'''
Created on 22 aug. 2014

@author: sjuul
'''
from urllib import unquote
import simplejson as json
from twisted.internet.defer import Deferred


class ResponseHandler(object):

    def __init__(self, connection, resultType):
        self._resultType = resultType
        self._connection = connection
        self._dfd = Deferred()

    @property
    def dfd(self):
        return self._dfd

    def onFailed(self, faillure, requestObj):
        self._dfd.errback(faillure)

    def onResponse(self, response, requestObj):
        if response.contentType == 'json':
            try:
                self.handleLoaded(self.loadJson(response), requestObj)
            except Exception as ex:
                self._dfd.errback(Exception(str(ex) + '\n' + response.msg))
        else:
            self._dfd.callback(response.msg)

    def handleLoaded(self, loaded, requestObj):
        self._dfd.callback(loaded)

    def loadJson(self, response):
        if response.charset:
            encoding = response.charset
        else:
            encoding = None
        return json.loads(response.msg, encoding=encoding)


class GoogleResponseHandler(ResponseHandler):

    def handleLoaded(self, loaded, requestObj):
        if 'error' in loaded:
            if 'errors' in loaded['error']:
                errorMessages = [item['message'] for item in loaded['error']['errors']]
                self._dfd.errback(Exception('\n'.join(errorMessages)))
            else:
                self._dfd.errback(Exception(json.dumps(loaded['error'])))
        else:
            self._onResponse(loaded, requestObj)

    def _onResponse(self, loaded, requestObj):
        if 'nextPageToken' in loaded:
            if 'httpUrlParams' not in queryParams:
                queryParams['httpUrlParams'] = {}
            queryParams['httpUrlParams']['pageToken'] = unquote(loaded['nextPageToken'])
            self._asyncHttpRequest(queryParams)
        else:
            self._finishUpResult(loaded, queryParams)

    def _loadResults(self, loaded, queryParams):
        resultType = queryParams['resultType']
        loadFunName = '_loadResults_' + resultType
        if hasattr(self, loadFunName):
            loadFun = getattr(self, loadFunName)
        else:
            loadFun = None
        if self._multipleResultsPossible(resultType):
            print loadFunName
            if hasattr(self, loadFunName)  and 'results' not in queryParams:
                queryParams['results'] = []
            if not loadFun:
                raise Exception('No load fun for')
            results = queryParams['results']
            results.extend(loadFun(loaded))
        else:
            if loadFun:
                queryParams['results'] = loadFun(loaded)
            else:
                queryParams['results'] = loaded

    def _finishUpResult(self, loaded, queryParams):
        if 'results' in queryParams:
            queryParams['dfdDone'].callback(queryParams['results'])
        else:
            queryParams['dfdDone'].callback(loaded)

    def _multipleResultsPossible(self, resultType):
        return resultType in ('multi')

    def _loadResults_multi(self, loaded):
        if loaded != 'Not Found':
            for k, v in loaded.iteritems():
                if isinstance(v, list):
                    for item in v:
                        yield item
