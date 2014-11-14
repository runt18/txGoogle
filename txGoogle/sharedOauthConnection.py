'''
Created on 15 jul. 2014

@author: sjuul
'''
from txGoogle.oAuthCredentialsConnection import OAuthCredentialsConnection
from txGoogle.sharedConnection import SharedConnection


class SharedOauthConnection(SharedConnection):

    AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'

    def __init__(self, clientId=None, clientSecret=None, credentialsFileName=None):
        super(SharedOauthConnection, self).__init__()
        self._clientId = clientId
        self._clientSecret = clientSecret
        self._credentialsFileName = credentialsFileName

    def registerScopes(self, scopes):
        if not hasattr(self, '_SCOPE'):
            self._SCOPE = ' '.join(scopes)
        else:
            self._SCOPE = ' '.join(set(self._SCOPE.split(' ')).union(set(scopes)))

    def connect(self):
        self._connHandler = OAuthCredentialsConnection(self.AUTH_URL, self.TOKEN_URL, clientId=self._clientId, clientSecret=self._clientSecret, credentialsFileName=self._credentialsFileName, scope=self._SCOPE, approval_prompt='force', access_type='offline', response_type='code')
        return self._connHandler._loadCredentials()

