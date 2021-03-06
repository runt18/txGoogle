'''
Created on 22 aug. 2014

@author: sjuul
'''
from txGoogle.request import Request
from txGoogle.responseHandler import ResponseHandler


class Service(object):

    def __init__(self, conn, *args, **kwargs):
        self._conn = conn
        if 'requestCls' in kwargs:
            self._requestCls = kwargs['requestCls']
        else:
            self._requestCls = Request
        if 'responseCls' in kwargs:
            self._responseCls = kwargs['responseCls']
        else:
            self._responseCls = ResponseHandler

    def _request(self, requestParams):
        responseHandler = self._responseCls(self._conn, requestParams.pop('resultType'))
        reqObj = self._requestCls(**requestParams)
        self._conn.request(reqObj, responseHandler)
        return responseHandler.dfd
