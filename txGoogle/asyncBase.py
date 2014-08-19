'''
Created on 15 jul. 2014

@author: sjuul
'''
from asyncOAuth import AsyncOAuthConnectionHandler
from twisted.internet.defer import Deferred
from twisted.internet import reactor
from urllib import unquote
import simplejson as json
import time


class AsyncBase(object):

    MAX_CONCURRENT_QUERIES = 20 - 5  # subtracting 5 because I saw connection closings when doing multiple requests
    REQUEST_RESEND_CHECK_INTERVAL = 2
    AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'

    def __init__(self, clientId=None, clientSecret=None, credentialsFileName=None, jsonHandleFun=None):
        if jsonHandleFun is None:
            jsonHandleFun = self._handleGoogleJson
        self._clientId = clientId
        self._clientSecret = clientSecret
        self._credentialsFileName = credentialsFileName
        self._jsonHandleFun = jsonHandleFun
        self._runningReqs = []
        self._connHandler = None

    def registerScopes(self, scopes):
        if not hasattr(self, '_SCOPE'):
            self._SCOPE = ' '.join(scopes)
        else:
            self._SCOPE = ' '.join(self._SCOPE.split(' ') + scopes)

    def connect(self):
        self._connHandler = AsyncOAuthConnectionHandler(self.AUTH_URL, self.TOKEN_URL, clientId=self._clientId, clientSecret=self._clientSecret, credentialsFileName=self._credentialsFileName, jsonHandleFun=self._jsonHandleFun, scope=self._SCOPE, approval_prompt='force', access_type='offline', response_type='code')

    def _asyncHttpRequest(self, queryParams):
        '''
        queryParams should contain all information required for making a request.
        This package of information can be used in order to handle follow up requests.

        Possible contents of queryParams used externally (ie the implementing class of AsyncBase):
        - resultType: should be provided so that the implementing class can decide how to handle the response correctly
        - httpBodyParams: parameters for the body of the http request in the form of a dict
        - httpUrlParams: parameters for the url of the http request in the form of a dict
        - httpHeaders: http headers in the form of a dict. AsyncOAuthConnectionHandler knows for example that when 'application/json' in headers['Content-Type'] it should json-dump the hhtpParams into the request body.
        - results: a variable to be used to build up the result. Most likely useful when doing pagination
        - url: this is the url where the request is sent to. This can contain parameters eg: https://www.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId} these parameters are expected to be available in the queryParams dict and are filled in just before the request is executed
        - "url parameters": as described above
        - method: http method; POST / GET / UPDATE ...

        Some of the contents of queryParams created internally:
        - dfdRequest: the deferred of the current running request
        - ts: the timestamp of when the last request was started
        - dfdDone: the deferred handed back to the caller. This is the external deferred. It should abstract away all internal follow ups of requests. dfdDone is returned by `_asyncHttpRequest` and should be returned to the requesting code

        '''
        if self._connHandler is None:
            self.connect()

        if 'resultType' not in queryParams:
            raise Exception('resultType is required in order to load the data correctly when the result comes in')
        if 'dfdDone' not in queryParams:
            queryParams['dfdDone'] = Deferred()
        if len(self._runningReqs) < self.MAX_CONCURRENT_QUERIES:
            dfdRequest = self._connHandler.httpRequest(
                #url=queryParams['url'].format(**queryParams),
                url=queryParams['url'].format(**queryParams.get('httpUrlParams', {})),
                urlParams=queryParams.get('httpUrlParams', {}),
                bodyParams=queryParams.get('httpBodyParams', {}),
                headers=queryParams.get('httpHeaders', {}),
                method=queryParams.get('method'),
                formEncode=queryParams.get('formEncode', False)
            )
            queryParams['dfdRequest'] = dfdRequest
            queryParams['ts'] = time.time()
            self._runningReqs.append(queryParams)
            dfdRequest.addCallback(self._handleResponse, queryParams)
            dfdRequest.addErrback(self._handleFailed, queryParams)
        else:
            reactor.callLater(self.REQUEST_RESEND_CHECK_INTERVAL, self._asyncHttpRequest, queryParams)
        return queryParams['dfdDone']

    def _handleFailed(self, faillure, queryParams):
        print faillure
        if queryParams in self._runningReqs:
            self._runningReqs.remove(queryParams)
            queryParams['dfdDone'].errback(faillure)
        else:
            # _handleResponse has been called. _handleResponse removes the queryParams from _runningReqs.
            # Thus when _handleFailed is called and queryParams not in self._runningReqs it is a response handling error.
            queryParams['dfdDone'].errback(Exception('Error in response handling: {}'.format(faillure)))

    def _handleResponse(self, loaded, queryParams):
        self._runningReqs.remove(queryParams)
        if not loaded:
            queryParams['dfdDone'].callback(None)
            return
        self._loadResults(loaded, queryParams)
        self._onResponse(loaded, queryParams)

    def _onResponse(self, loaded, queryParams):
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

    def _handleGoogleJson(self, msg, dfd):
        loaded = json.loads(msg)
        if 'error' in loaded:
            if 'errors' in loaded['error']:
                errorMessages = [item['message'] for item in loaded['error']['errors']]
                dfd.errback(Exception('\n'.join(errorMessages)))
            else:
                dfd.errback(Exception(json.dumps(loaded['error'])))
        else:
            dfd.callback(loaded)

    def _multipleResultsPossible(self, resultType):
        return resultType in ('multi')

    def _loadResults_multi(self, loaded):
        if loaded != 'Not Found':
            for k, v in loaded.iteritems():
                if isinstance(v, list):
                    for item in v:
                        yield item
