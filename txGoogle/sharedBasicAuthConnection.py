'''
Created on Nov 4, 2014

@author: sjuul
'''
from txGoogle.sharedConnection import SharedConnection
from txGoogle.basicAuthCredentialsConnection import BasicAuthCredentialsConnection


class SharedBasicAuthConnection(SharedConnection):

    def __init__(self, userName, password):
        super(SharedBasicAuthConnection, self).__init__()
        self._connHandler = BasicAuthCredentialsConnection(userName, password)

    def connect(self):
        if self._connHandler is None:
            raise Exception('No connHandler')
