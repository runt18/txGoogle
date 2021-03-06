'''
Created on 22 aug. 2014

@author: sjuul
'''
import simplejson as json
from twisted.internet.defer import Deferred
from twisted.internet.defer import logError
from twisted.internet.defer import passthru
from twisted.python import log


class ResponseHandler(object):

    def __init__(self, connection, resultType):
        self._resultType = resultType
        self._connection = connection
        self._dfd = Deferred()
        self._ebAdded = False

    @property
    def dfd(self):
        return self._dfd

    def onFailed(self, faillure, requestObj):
        log.msg('Failed request {}'.format(requestObj))
        self._dfd.errback(faillure)

    def _logErr(self, fail):
        log.err(fail)
        print fail
        raise fail

    def _hasErrback(self):
        if self._ebAdded:
            return True
        if len(self._dfd.callbacks) == 0:
            return False
        return self._dfd.callbacks[0][1][0] != passthru

    def _checkForExistingEbs(self):
        if not self._hasErrback():
            self._dfd.addErrback(logError)
            self._ebAdded = True

    def onResponse(self, response, requestObj):
        if response is None:
            self._dfd.errback(Exception('None response'))
        self._checkForExistingEbs()
        if response.contentType == 'application/json':
            try:
                self.handleLoaded(self.loadJson(response), requestObj)
            except Exception as ex:
                self._dfd.errback(Exception(str(ex) + '\n' + response.msg))
        elif response.contentType == 'text/csv':
            try:
                self.handleLoaded(self.loadCsv(response), requestObj)
            except Exception as ex:
                self._dfd.errback(Exception(str(ex) + '\n' + response.msg))
        else:
            self._dfd.callback(response.msg)

    def handleLoaded(self, loaded, requestObj):
        self._onResponse(loaded, requestObj)

    def loadJson(self, response):
        if response.charset:
            encoding = response.charset
        else:
            encoding = None
        return json.loads(response.msg, encoding=encoding)

    def loadCsv(self, response):
        return [[cell for cell in line.split(',')] for line in response.msg.split('\n')[:-1]]
        # return [cell for line in response.msg.split('\n') for cell in line.split(',')]

    def _loadResults(self, loaded, requestObj):
        loadFunName = '_loadResults_' + self._resultType
        if hasattr(self, loadFunName):
            loadFun = getattr(self, loadFunName)
            loadFun(loaded)
        else:
            self._result = loaded

    def _loadResults_multi(self, loaded):
        if self._result is None:
            self._result = []
        if loaded != 'Not Found':
            for v in loaded.itervalues():
                if isinstance(v, list):
                    self._result.extend(v)

    def _onResponse(self, loaded, requestObj):
        self._loadResults(loaded, requestObj)
        self._dfd.callback(self._result)
