'''
Created on 22 aug. 2014

@author: sjuul
'''
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
