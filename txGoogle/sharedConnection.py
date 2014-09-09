'''
Created on 15 jul. 2014

@author: sjuul
'''
from asyncOAuth import AsyncOAuthConnectionHandler
from twisted.internet import reactor


class SharedConnection(object):

    MAX_CONCURRENT_QUERIES = 20 - 5  # subtracting 5 because I saw connection closings when doing multiple requests
    REQUEST_RESEND_CHECK_INTERVAL = 2
    AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'

    def __init__(self, clientId=None, clientSecret=None, credentialsFileName=None):
        self._clientId = clientId
        self._clientSecret = clientSecret
        self._credentialsFileName = credentialsFileName
        self._runningReqs = []
        self._connHandler = None

    def registerScopes(self, scopes):
        if not hasattr(self, '_SCOPE'):
            self._SCOPE = ' '.join(scopes)
        else:
            self._SCOPE = ' '.join(self._SCOPE.split(' ') + scopes)

    def connect(self):
        self._connHandler = AsyncOAuthConnectionHandler(self.AUTH_URL, self.TOKEN_URL, clientId=self._clientId, clientSecret=self._clientSecret, credentialsFileName=self._credentialsFileName, scope=self._SCOPE, approval_prompt='force', access_type='offline', response_type='code')

    def request(self, requestObj, responseHandler):
        if self._connHandler is None:
            self.connect()
        if len(self._runningReqs) < self.MAX_CONCURRENT_QUERIES:
            dfdRequest = self._connHandler.request(requestObj)
            self._runningReqs.append(requestObj)
            dfdRequest.addCallback(self._handleResponse, requestObj, responseHandler)
            dfdRequest.addErrback(self._handleFailed, requestObj, responseHandler)
        else:
            reactor.callLater(self.REQUEST_RESEND_CHECK_INTERVAL, self._asyncHttpRequest, requestObj, responseHandler)
        return responseHandler.dfd

    def _handleResponse(self, response, requestObj, responseHandler):
        self._runningReqs.remove(requestObj)
        responseHandler.onResponse(response, requestObj)

    def _handleFailed(self, faillure, requestObj, responseHandler):
        responseHandler.onFailed(faillure, requestObj)
