'''
Created on 4 nov. 2014

@author: sjuul
'''
from txGoogle.asyncHttp import AsyncHttp
import time


class BasicAuthCredentialsConnection(AsyncHttp):

    def __init__(self, userName, password):
        super(BasicAuthCredentialsConnection, self).__init__()
        self._userName = userName
        self._password = password

    def request(self, requestObj):
        requestObj._startTs = time.time()
        requestObj.setBasicCredentials(self._userName, self._password)
        return self.asyncHttpRequest(requestObj)
