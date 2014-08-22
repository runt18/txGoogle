'''
Created on 22 aug. 2014

@author: sjuul
'''
from txGoogle.utils import leaveOutNulls
from txGoogle.googleServiceRequest import GoogleServiceRequest


class Service(object):

    def __init__(self, conn, *args, **kwargs):
        self._conn = conn
        if 'requestCls' in kwargs:
            self._requestCls = kwargs['requestCls']
        else:
            self._requestCls = GoogleServiceRequest
        if 'responseCls' in kwargs:
            self._responseCls = kwargs['resonseCls']
        else:
            self._responseCls = kwargs['resonseCls']

    def _request(self, requestParams):
        respObj = self._responseCls()
        reqObj = self._requestCls(respObj, **leaveOutNulls(requestParams))
        self._conn.request(reqObj)
        return respObj.dfd
