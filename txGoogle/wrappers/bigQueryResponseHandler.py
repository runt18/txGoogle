'''
Created on 9 sep. 2014

@author: sjuul
'''
from txGoogle.googleResponseHandler import GoogleResponseHandler
import simplejson as json
from twisted.internet import reactor


class BigQueryResponseHandler(GoogleResponseHandler):

    VALUE_FORMAT_FUNS = {
        'STRING': lambda s: s,
        'FLOAT': lambda s: float(s) if s else s,
        'TIMESTAMP': lambda s: int(float(s)) if s else s,
        'INTEGER': lambda s: int(s) if s else s
    }

    def loadJson(self, response):
        '''
        Overriding the json loading as splitting is much faster when dealing with records
        '''
        msg = response.msg
        rowsStr = '"rows": [\n  {\n   "f": [\n    {\n     "v": "'
        rowsParsed = []
        if rowsStr in msg:
            startPart, endPart = msg.split(rowsStr)
            rows, endPart = endPart.split('"\n    }\n   ]\n  }\n ],\n "totalBytesProcessed"')
            msg = startPart + ' "totalBytesProcessed"' + endPart
            rowSepPattern = '"\n    }\n   ]\n  },\n  {\n   "f": [\n    {\n     "v": "'
            colSepPattern = '"\n    },\n    {\n     "v": "'
            rowsParsed = [row.split(colSepPattern) for row in rows.split(rowSepPattern)]
        loaded = json.loads(msg)
        loaded['rows'] = rowsParsed
        return loaded

    def _onResponse(self, loaded, requestObj):
        if 'jobReference' in loaded and 'jobId' in loaded['jobReference']:
            self._handleJobResult(loaded, requestObj)
        else:
            super(BigQueryResponseHandler, self)._onResponse(loaded, requestObj)

    def _handleJobResult(self, loaded, requestObj):
        requestObj.setUrlParam('jobId', loaded['jobReference']['jobId'])
        if 'pageToken' in loaded:
            requestObj.setUrlParam('pageToken', loaded['pageToken'])
            if 'jobComplete' in loaded and loaded['jobComplete']:
                assert self._result is None, 'Already have loaded results?'
                self._dfd.callback(loaded)
            else:
                self._getQueryResults(requestObj)
        elif 'status' in loaded:
            self._handleJobStatus(loaded, requestObj)
        else:
            assert self._result is None, 'Already have loaded results?'
            self._dfd.callback(loaded)

    def _getQueryResults(self, requestObj):
        '''
        Adjusts the queryParams so that we can get the rest of the results
        '''
        jobId = requestObj.getUrlParam('jobId')
        if jobId is None:
            raise Exception('jobId required when continuing reading query results')
        queryParams = {
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/queries/{jobId}',
            'method': 'GET',
            'resultType': 'rows',
            'httpUrlParams': {
                'jobId': jobId,
                'maxResults': requestObj.getUrlParam('maxResults'),
                'pageToken': requestObj.getUrlParam('pageToken')
            }
        }
        return self._request(queryParams, responseObj=self)

    def _handleJobStatus(self, loaded, requestObj):
        sts = loaded['status']['state']
        if sts == 'DONE':
            if 'errors' in loaded['status'] and len(loaded['status']['errors']) > 0:
                self._dfd.errback(Exception('Failed: {}'.format(', '.join(loaded['status']['errors']))))
            self._dfd.callback(self._result)
        elif sts == 'RUNNING':
            if not hasattr(requestObj, 'recheckIntervals'):
                requestObj.recheckIntervals = [2, 5, 10, 15, 30, 30, 30]
            if len(requestObj.recheckIntervals) > 0:
                recheckInterval = requestObj.recheckIntervals.pop(0)
                reactor.callLater(recheckInterval, self._request, requestObj)
            else:
                self._dfd.errback(Exception('Timed out'))
        else:
            raise Exception('Unknown job response format, {}'.format(sts))

    def _request(self, requestObj):
        self._conn.request(requestObj, self)
        return self._dfd

    def _loadResults_tables(self, loaded):
        if 'tables' in loaded:
            if self._result is None:
                self._result = []
            self._result.extend(loaded['tables'])

    def _loadResults_job(self, loaded):
        self._result = loaded

    def _loadResults_rows(self, results):
        if self._result is None:
            self._result = []
        if 'rows' in results:
            if 'schema' not in results:
                if len(results.get('rows', [])) > 0:
                    raise Exception('Expected schema')
                else:
                    return
            columns = results['schema']['fields']
            for row in results['rows']:
                newRows = [self.VALUE_FORMAT_FUNS[itemColumn['type']](item) for item, itemColumn in zip(row, columns)]
                self._result.extend(newRows)
            del results['rows']

    '''
    def _multipleResultsPossible(self, resultType):
        return resultType in ['tables', 'rows']
    '''

    def handleLoaded(self, loaded, requestObj):
        if 'error' in loaded:
            if 'errors' in loaded['error']:
                errorMessages = [item['message'] for item in loaded['error']['errors']]
                exMsg = '\n'.join(errorMessages)
                if 'FROM clause with table wildcards matches no table' in exMsg:
                    self._onResponse({'kind': 'bigquery#queryResponse', 'rows': [], 'message': exMsg}, requestObj)
                else:
                    self._dfd.errback(Exception(exMsg))
            else:
                self._dfd.errback(Exception(json.dumps(loaded['error'])))
        else:
            self._onResponse(loaded, requestObj)
