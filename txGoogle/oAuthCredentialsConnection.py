'''
Created on 14 jul. 2014

@author: sjuul
'''
from twisted.internet.defer import Deferred
from twisted.internet.defer import succeed
from asyncUtils import ignoreFirstArg
from txGoogle.request import Request
from asyncHttp import AsyncHttp
from twisted.python import log
from urllib import urlencode
import simplejson as json
import webbrowser
import logging
import time
import os


'''
Currently implemented as installed app. This doesn't require us to run a web server.
The difference between "installed app" and webserver is that now we need to copy-paste the oauth token into our console,
when running a webserver the oauth endpoint will send the token to the webserver.
The rest of the grant process is the same.

Reference: https://developers.google.com/accounts/docs/OAuth2InstalledApp
Playground: https://developers.google.com/oauthplayground/

If you want to understand the "flow" of oauth the playground will take you through the steps
'''


class OAuthCredentialsConnection(AsyncHttp):

    def __init__(self, authUrl, tokenUrl, scope, clientId=None, clientSecret=None, credentialsFileName=None, redirect_uri='urn:ietf:wg:oauth:2.0:oob', **grantKwargs):
        super(OAuthCredentialsConnection, self).__init__()
        self._grantUrl = authUrl
        self._tokenUrl = tokenUrl
        self._clientId = clientId
        self._clientSecret = clientSecret
        self._redirectUri = redirect_uri
        self._grantKwargs = grantKwargs
        self._grantKwargs['redirect_uri'] = redirect_uri
        self._grantKwargs['client_id'] = clientId
        self._grantKwargs['scope'] = scope
        self._hasScopes = not (scope is None or len(scope) == 0)
        self._credentialsFileName = credentialsFileName
        if credentialsFileName is None:
            raise Exception('No credentialsFileName is specified')
        self._getAccessCredsDfd = None
        self._credentialsDct = None
        self._scopesCompared = False
        self._loadCredentials()

    def _getAccessCredentials(self, authCode=None, refreshToken=None):
        if self._getAccessCredsDfd is None:
            self._getAccessCredsDfd = Deferred()
        else:
            return self._getAccessCredsDfd
        if not self._hasScopes:
            return self._getAccessCredsDfd.callback('Ok')
        if refreshToken:
            tokenParams = {
                'client_id': self._clientId,
                'client_secret': self._clientSecret,
                'grant_type': 'refresh_token',
                'refresh_token': refreshToken
            }
        else:
            if authCode is None:
                url = self._grantUrl + '?' + urlencode(self._grantKwargs)
                print url
                webbrowser.open(url)
                authCode = raw_input('\nCODE:')
            tokenParams = {
                'code': authCode,
                'redirect_uri': self._redirectUri,
                'client_id': self._clientId,
                'client_secret': self._clientSecret,
                'grant_type': 'authorization_code'
            }
        req = Request(url=self._tokenUrl, httpUrlParams=tokenParams, method='POST', formEncode=True)
        dfd = self.asyncHttpRequest(req)
        dfd.addCallback(self.handleToken, refreshToken=refreshToken)
        return self._getAccessCredsDfd

    def handleToken(self, responseObj, refreshToken):
        log.msg('Received token dict', logLevel=logging.INFO)
        loaded = json.loads(responseObj.msg)
        if 'error' in loaded:
            self._getAccessCredsDfd.errback(loaded['error'])
        if 'id_token' in loaded:
            print 'found id token'
        self._credentialsDct = loaded
        self._credentialsDct['scopes'] = self._grantKwargs['scope'].split(' ')
        self._credentialsDct['expirationTimestamp'] = int(time.time()) + self._credentialsDct['expires_in']
        if refreshToken:
            self._credentialsDct['refresh_token'] = refreshToken
        parentFolder = os.path.dirname(self._credentialsFileName)
        if parentFolder and not os.path.exists(parentFolder):
            os.makedirs(parentFolder)
        fl = open(self._credentialsFileName, 'w')
        json.dump(self._credentialsDct, fl)
        fl.close()
        self._getAccessCredsDfd.callback('Ok')
        return 'Ok'

    def _credentialsDictIsValid(self):
        if not self._scopesCompared:
            self._scopesCompared = True
            missing = set(self._grantKwargs['scope'].split(' ')) - set(self._credentialsDct.get('scopes', []))
            if missing:
                if 'refresh_token' in self._credentialsDct:
                    del self._credentialsDct['refresh_token']
                if 'access_token' in self._credentialsDct:
                    del self._credentialsDct['access_token']
                log.msg('Required scopes have changed', logLevel=logging.INFO)
                return False
        if 'expirationTimestamp' not in self._credentialsDct:
            log.msg('Missing expirationTimestamp', logLevel=logging.INFO)
            return False
        if 'refresh_token' not in self._credentialsDct:
            log.msg('Missing refresh_token', logLevel=logging.INFO)
            return False
        return True

    def _checkCredentialsDct(self):
        if not self._credentialsDictIsValid():
            return self._getAccessCredentials()
        elif self._credentialsDct['expirationTimestamp'] < int(time.time() + 100):
            if self._getAccessCredsDfd is None or self._getAccessCredsDfd.called:
                self._getAccessCredsDfd = None
                log.msg('Grant expired, refreshing', logLevel=logging.INFO)
                return self._getAccessCredentials(refreshToken=self._credentialsDct['refresh_token'])
            else:
                return self._getAccessCredsDfd
        else:
            return succeed('grant still valid')

    def _loadCredentials(self):
        if self._credentialsDct:
            return self._checkCredentialsDct()
        elif self._getAccessCredsDfd:
            return self._getAccessCredsDfd
        elif os.path.exists(self._credentialsFileName):
            credsFile = open(self._credentialsFileName, 'r')
            creds = json.load(credsFile)
            credsFile.close()
            self._credentialsDct = creds
            return self._checkCredentialsDct()
        else:
            return self._getAccessCredentials()

    def request(self, requestObj):
        requestObj._startTs = time.time()
        dfd = self._loadCredentials()
        if self._hasScopes:
            @dfd.addCallback
            def injectAccesToken(dummy):
                requestObj.setToken(self._credentialsDct['access_token'])

        dfd.addCallback(ignoreFirstArg, self.asyncHttpRequest, requestObj)
        return dfd
