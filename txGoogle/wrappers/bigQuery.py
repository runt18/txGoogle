'''
Created on 26 jun. 2014

@author: sjuul
'''
from twisted.internet import reactor
import simplejson as json
from txGoogle.asyncUtils import mapFunToItems
from txGoogle.asyncUtils import mapFunToItemsSequentially
from twisted.internet.defer import fail
from txGoogle.services.bigquery_ import Bigquery
import re

'''
Reference: https://developers.google.com/bigquery/docs/reference/v2/
'''

DEFAULT_BQ_CHUNK_SIZE = 1000


def splitRecordsToChuncks(records):
    for i in xrange(0, len(records), DEFAULT_BQ_CHUNK_SIZE):
        yield records[i:i + DEFAULT_BQ_CHUNK_SIZE]


def loadWithoutJson(line):
    nCharsPrefix = 7
    nCharsEnd = 2

    nCharsRowPrefix = 8
    nCharsRowEnd = 3

    return [row[nCharsRowPrefix:-nCharsRowEnd].split('"}, {"v": "') for row in line[nCharsPrefix:-nCharsEnd].split('}, {"f": ')]


class BigQuery(Bigquery):

    VALUE_FORMAT_FUNS = {
        'STRING': lambda s: s,
        'FLOAT': lambda s: float(s) if s else s,
        'TIMESTAMP': lambda s: int(float(s)) if s else s,
        'INTEGER': lambda s: int(s) if s else s
    }

    def __init__(self, *args, **kwargs):
        kwargs['jsonHandleFun'] = self._handleBqJson
        super(Bigquery, self).__init__(*args, **kwargs)

    def _loadBqRows(self, msg):
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

    def _handleBqJson(self, msg, dfd):
        r = re.search(r'"kind": "(.*?)"', msg)
        if r is not None and r.groups()[0] == 'bigquery#queryResponse':
            loaded = self._loadBqRows(msg)
        else:
            loaded = json.loads(msg)

        if 'error' in loaded:
            if 'errors' in loaded['error']:
                errorMessages = [item['message'] for item in loaded['error']['errors']]
                dfd.errback(Exception('\n'.join(errorMessages)))
            else:
                dfd.errback(Exception(json.dumps(loaded['error'])))
        else:
            dfd.callback(loaded)

    def _onResponse(self, loaded, queryParams):
        if 'jobReference' in loaded and 'jobId' in loaded['jobReference']:
            self._handleJobResult(loaded, queryParams)
        else:
            self.conn._onResponse(self, loaded, queryParams)

    def _handleJobStatus(self, loaded, queryParams):
        sts = loaded['status']['state']
        if sts == 'DONE':
            if 'errors' in loaded['status'] and len(loaded['status']['errors']) > 0:
                queryParams['dfdDone'].errback(Exception('Failed: {}'.format(', '.join(loaded['status']['errors']))))
            elif 'results' in queryParams:
                queryParams['dfdDone'].callback(queryParams['results'])
            else:
                queryParams['dfdDone'].callback('Ok')
        elif sts == 'RUNNING':
            if 'recheckIntervals' not in queryParams:
                queryParams['recheckIntervals'] = [2, 5, 10, 15, 30, 30, 30]
            if len(queryParams['recheckIntervals']) > 0:
                recheckInterval = queryParams['recheckIntervals'].pop(0)
                reactor.callLater(recheckInterval, self._getJobStatus, queryParams)
            else:
                queryParams['dfdDone'].errback(Exception('Timed out'))
        else:
            raise Exception('Unknown job response format, {}'.format(sts))

    def _handleJobResult(self, loaded, queryParams):
        queryParams['jobId'] = loaded['jobReference']['jobId']
        if 'pageToken' in loaded:
            queryParams['pageToken'] = loaded['pageToken']
            if 'jobComplete' in loaded and loaded['jobComplete']:
                self._finishUpResult(loaded, queryParams)
            else:
                self._getQueryResults(queryParams)
        elif 'status' in loaded:
            self._handleJobStatus(loaded, queryParams)
        else:
            #Normal query which is done. Queries produce jobIds.
            self._finishUpResult(loaded, queryParams)

    def _loadResults_tables(self, loaded):
        for table in loaded['tables']:
            yield table

    def _loadResults_job(self, loaded):
        return loaded

    def _loadResults_rows(self, results):
        if 'rows' in results:
            if 'schema' not in results:
                if len(results.get('rows', [])) > 0:
                    raise Exception('Expected schema')
                else:
                    return
            columns = results['schema']['fields']
            for row in results['rows']:
                yield [self.VALUE_FORMAT_FUNS[itemColumn['type']](item) for item, itemColumn in zip(row, columns)]
            del results['rows']

    def _multipleResultsPossible(self, resultType):
        return resultType in ['tables', 'rows']

    def createTable(self, projectId, datasetId, tableId, fields, expirationMiliTs=None, friendlyName=None, description=None):
        httpBodyParams = {
          'kind': 'bigquery#table',
          'tableReference': {
            'projectId': projectId,
            'datasetId': datasetId,
            'tableId': tableId
          },
          'schema': {
            'fields': fields
          }
        }
        queryParams = {
          'httpBodyParams': httpBodyParams,
          'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables',
          'method': 'POST',
          'resultType': 'table',
          'datasetId': datasetId,
          'projectId': projectId
        }
        if friendlyName:
            httpBodyParams['friendlyName'] = friendlyName
        if description:
            httpBodyParams['description'] = description
        if expirationMiliTs:
            httpBodyParams['expirationTime'] = expirationMiliTs
        return self._asyncHttpRequest(queryParams)

    def renameTable(self, projectId, datasetId, oldTableId, newTableId):
        dfd = self.copyTable(projectId, datasetId, oldTableId, projectId, datasetId, newTableId)

        @dfd.addCallback
        def onTableCopied(dummy):
            self.deleteTable(projectId, datasetId, oldTableId)
        return dfd

    def copyTable(self, srcProjectId, srcDatasetId, srcTableId, dstProjectId, dstDatasetId, dstTableId):
        jobData = {
             'projectId': srcProjectId,
             'configuration': {
                'copy': {
                    'sourceTable': {
                    'projectId': srcProjectId,
                    'datasetId': srcDatasetId,
                    'tableId': srcTableId
                  },
                    'destinationTable': {
                    'projectId': dstProjectId,
                    'datasetId': dstDatasetId,
                    'tableId': dstTableId
                  }
               }
            }
        }
        queryParams = {
            'projectId': projectId,
            'method': 'POST',
            'httpBodyParams': jobData,
            'resultType': 'job',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs'
        }
        return self._asyncHttpRequest(queryParams)

    def deleteTable(self, projectId, datasetId, tableId):
        queryParams = {
            'projectId': projectId,
            'datasetId': datasetId,
            'tableId': tableId,
            'method': 'DELETE',
            'resultType': 'delete',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}'
        }
        return self._asyncHttpRequest(queryParams)

    def getTable(self, projectId, datasetId, tableId):
        queryParams = {
            'projectId': projectId,
            'datasetId': datasetId,
            'tableId': tableId,
            'method': 'GET',
            'resultType': 'table',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}'
        }
        return self._asyncHttpRequest(queryParams)

    def getTableData(self, projectId, datasetId, tableId):
        queryParams = {
            'projectId': projectId,
            'datasetId': datasetId,
            'tableId': tableId,
            'resultType': 'rows',
            'method': 'GET',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data'
        }
        return self._asyncHttpRequest(queryParams)

    def getTables(self, projectId, datasetId):
        queryParams = {
            'projectId': projectId,
            'datasetId': datasetId,
            'method': 'GET',
            'resultType': 'tables',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables'
        }
        return self._asyncHttpRequest(queryParams)

    def _ExtractTableIds(self, tables):
        return [table['tableReference']['tableId'] for table in tables]

    def getTableIds(self, projectId, datasetId):
        dfd = self.getTables(projectId, datasetId)
        dfd.addCallback(self._ExtractTableIds)
        return dfd

    def query(self, projectId, datasetId, queryStr):
        dfd = super(Bigquery, self).query(projectId, datasetId, queryStr)
        dfd.addErrback(self._handleQryError)
        return dfd

    def _handleQryError(self, err):
        if hasattr(err, 'value') and hasattr(err.value, 'message'):
            try:
                if 'FROM clause with table wildcards matches no table' in err.value.message:
                    return []
            except:
                return fail(err)
        return fail(err)

    def _getQueryResults(self, queryParams):
        '''
        Adjusts the queryParams so that we can get the rest of the results
        '''
        if 'jobId' not in queryParams:
            raise Exception('jobId required when continuing reading query results')
        queryParams['httpUrlParams'] = {'kind': 'bigquery#getQueryResultsResponse'}
        if 'maxResults' in queryParams:
            queryParams['httpUrlParams']['maxResults'] = queryParams['maxResults']
        if 'pageToken' in queryParams:
            queryParams['httpUrlParams']['pageToken'] = queryParams['pageToken']
        queryParams['method'] = 'GET'
        if 'httpHeaders' in queryParams:
            del queryParams['httpHeaders']
        queryParams['url'] = 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/queries/{jobId}'
        queryParams['resultType'] = 'rows'
        return self._asyncHttpRequest(queryParams)

    def _getJobStatus(self, queryParams):
        if 'jobId' not in queryParams:
            raise Exception('jobId required')
        queryParams['method'] = 'GET'
        if 'httpHeaders' in queryParams:
            del queryParams['httpHeaders']
        queryParams['url'] = 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/jobs/{jobId}'
        queryParams['resultType'] = 'job'
        return self._asyncHttpRequest(queryParams)

    def getJob(self, projectId, jobId):
        return self._getJobStatus({'jobId': jobId, 'projectId': projectId})

    def _insertChunck(self, records, projectId, datasetId, tableId):
        queryParams = {
            'datasetId': datasetId,
            'projectId': projectId,
            'tableId': tableId,
            'httpBodyParams': {
                'kind': 'bigquery#tableDataInsertAllRequest',
                'rows': []
            },
            'resultType': 'rows',
            'method': 'POST',
            'url': 'https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll'
        }
        for record in records:
            queryParams['httpBodyParams']['rows'].append({'json': record})
        return self._asyncHttpRequest(queryParams)

    def streamingInsertParallel(self, projectId, datasetId, tableId, records):
        return mapFunToItems(splitRecordsToChuncks(records), self._insertChunck, projectId=projectId, datasetId=datasetId, tableId=tableId)

    def streamingInsertSequential(self, projectId, datasetId, tableId, records):
        return mapFunToItemsSequentially(splitRecordsToChuncks(records), self._insertChunck, projectId=projectId, datasetId=datasetId, tableId=tableId)


if __name__ == '__main__':
    aBq = AsyncBigQuery('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'asyncBqCredentials.json')

    projectId = 'detect-analyze-notify-01a'
    datasetId = 'cust_711f9f25ed85'
    tableId = 'perf_201406_005056ad452d'  #'perf_201406_d05fd522b2f5'


    '''projectId = 'over-sight'
    datasetId = 'cust_e6b3265a8031'
    tableId = 'log_201407'''
    #ProbeName, Type, ItemName, PropertyName, Value, TimeStamp
    #queryStr = 'SELECT * FROM [{}.{}] where message contains \'\\n\' limit 10'.format(datasetId, tableId)
    # queryStr = "SELECT probeName, checkName, type, itemName, propertyName, value, timestamp\n        FROM TABLE_QUERY(cust_23eb8fd09fbc, 'table_id CONTAINS \"perf_\" AND table_id CONTAINS \"_1e0895f63693\" AND INTEGER(SUBSTR(table_id, 6, 6)) >= 201408 AND INTEGER(SUBSTR(table_id, 6, 6)) <= 201408')\n        WHERE timestamp > 1407315364000000\n        AND timestamp < 1408006564000000\n        ORDER BY probeName, checkName, type, itemName, propertyName, timestamp"
    queryStr = "SELECT * FROM TABLE_QUERY(cust_23eb8fd09fbc, 'table_id CONTAINS \"log_\" AND INTEGER(SUBSTR(table_id, 5, 6)) >= 201308 AND INTEGER(SUBSTR(table_id, 5, 6)) <= 201408') WHERE (LogType = 8)"
    dfds = []
    #dfds.append(aBq.getJob(projectId, 'job_VJo4zEhFOUNZ5lmPGonPcOp1OJE'))
    dfds.append(aBq.query(projectId, datasetId, queryStr))
    #dfds.append(aBq.getTableData(projectId, datasetId, tableId))
    # dfds.append(aBq.getTables(projectId, datasetId))
    #dfds.append(aBq.getTable(projectId, datasetId, tableId))
    #dfds.append(aBq.getTables(projectId, datasetId))
    # dfds.append(aBq.createTable(projectId, datasetId, tableId, fields, expirationMiliTs, friendlyName, description))

    # dfds.append(aBq.copyTable(projectId, datasetId, tableId, projectId, datasetId, tableId + '_2'))
    # dfds.append(aBq.deleteTable(projectId, datasetId, tableId + '_2'))
    # dfds.append(aBq.renameTable(projectId, datasetId, tableId + '_2', tableId))

    datasetId = 'testdataset'
    tableId = 'testtable1'

    #dfds.append(aBq.createTable(projectId, datasetId, tableId, {}))
    # records = [{'fieldname': str(a)} for a in xrange(1000)]
    #dfds.append(aBq.streamingInsertParallel(projectId, datasetId, tableId, records))
    #dfds += aBq.streamingInsertSequential(projectId, datasetId, tableId, records)
    '''from generic.osgoogle.asyncUtils import mapFunToItems
    from twisted.internet.defer import succeed

    def renameFun(tableId, projectId, datasetId):
        if 'perf_' not in tableId:
            return succeed('Skipped')
        splitted = tableId.split('_')
        newtableId = '_'.join([splitted[0], splitted[2], splitted[1]])
        return aBq.renameTable(projectId, datasetId, tableId, newtableId)
    dfdGetTables = aBq.getTableIds(projectId, datasetId)
    dfdGetTables.addCallback(mapFunToItems, renameFun, projectId, datasetId)
    dfds.append(dfdGetTables)'''

    from generic.osgoogle.asyncUtils import addPrintCbs
    addPrintCbs(dfds)
    reactor.run()
