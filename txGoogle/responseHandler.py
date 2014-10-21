'''
Created on 22 aug. 2014

@author: sjuul
'''
import simplejson as json
from twisted.internet.defer import Deferred
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
        self._dfd.errback(faillure)

    def _logErr(self, fail):
        log.err()
        raise fail

    def _hasErrback(self):
        if self._ebAdded:
            return True
        if len(self._dfd.callbacks) == 0:
            return False
        return self._dfd.callbacks[0][1][0] != passthru

    def _checkForExistingEbs(self):
        if not self._hasErrback():
            self._dfd.addErrback(self._logErr)
            self._ebAdded = True

    def onResponse(self, response, requestObj):
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
        self._dfd.callback(loaded)

    def loadJson(self, response):
        if response.charset:
            encoding = response.charset
        else:
            encoding = None
        return json.loads(response.msg, encoding=encoding)

    def loadCsv(self, response):
        return [[cell for cell in line.split(',')] for line in response.msg.split('\n')[:-1]]
        # return [cell for line in response.msg.split('\n') for cell in line.split(',')]
