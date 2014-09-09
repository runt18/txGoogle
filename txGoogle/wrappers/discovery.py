'''
Created on 15 aug. 2014

@author: sjuul
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'oversight', 'shared'))
from generic.fileUtils import preparePathForFile
from txGoogle.asyncUtils import printCb, mapFunToItems, ignoreFirstArg
import json
from twisted.internet.defer import DeferredList
from txGoogle.asyncApisGenerator import generateCode
from txGoogle.utils import leaveOutNulls
from txGoogle.sharedConnection import SharedConnection
from txGoogle.service import Service

class Apis(Service):
    def __init__(self, conn, *args, **kwargs):
        super(Apis, self).__init__(conn, *args, **kwargs)

    def getRest(self, api, version, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None):
        '''Retrieve the description of a particular version of an api.'''
        queryParams = {
            'url': 'https://www.googleapis.com/discovery/v1/apis/{api}/{version}/rest',
            'method': 'GET',
            'resultType': 'dummy',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'api': api,
                'version': version,
            },
            'httpBodyParams': {
            },
        }
        return self._request(leaveOutNulls(queryParams))

    def list(self, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, name=None, preferred=None):
        '''Retrieve the list of APIs supported at this endpoint.'''
        queryParams = {
            'url': 'https://www.googleapis.com/discovery/v1/apis',
            'method': 'GET',
            'resultType': 'dummy',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'name': name,
                'preferred': preferred,
            },
            'httpBodyParams': {
            },
        }
        return self._request(leaveOutNulls(queryParams))


class Discovery(Service):
    '''Lets you discover information about other Google APIs, such as what APIs are available, the resource and method details for each API.'''
    _DEFAULT_SCOPES = ['']
    
    def __init__(self, conn=None, scopes=None):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        self.apis = Apis(conn)



class DiscoveryWrapper(Discovery):
    _APIDOCS_PATH = '../apiFiles'

    def getList(self):
        return self.apis.list(preferred=True)

    def downloadPreferred(self, apiNames=None):
        '''Download the specified api's docs. If no apiNames are given all apiFiles are downloaded'''
        dfd = self.apis.list(preferred=True)

        #dfd.addCallback(mapFunToItems, fun)
        @dfd.addCallback
        def fun(discoveryList):
            dfdLst = []
            for discoveryItem in discoveryList['items']:
                if apiNames:
                    if not discoveryItem['name'] in apiNames:
                        continue
                dfdLst.append(self.download(discoveryItem['name'], discoveryItem['version']))
            dfdL = DeferredList(dfdLst)
            return dfdL
        return dfd

    def download(self, apiName, version):
        dfd = self.apis.getRest(apiName, version)

        @dfd.addCallback
        def fun(contents):
            filePath = '{}/{}.json'.format(self._APIDOCS_PATH, apiName)
            filePath = os.path.abspath(filePath)
            preparePathForFile(filePath)
            json.dump(contents, open(filePath, 'w'))
            print 'downloaded {} {}'.format(apiName, version)
        return dfd


if __name__ == '__main__':
    from twisted.internet import reactor
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../AsyncAllCredentials.json')
    downloader = DiscoveryWrapper(conn)
    conn.connect()
    serviceList = ['datastore', 'bigquery', 'gmail']
    dfd = downloader.downloadPreferred(serviceList)
    #dfd = downloader.apis.getRest('datastore', 'v1beta2')
    #@dfd.addCallback
    #def fun(contents):
    #    print contents

    #dfd.addCallback(ignoreFirstArg, generateCode, serviceList)
    #dfd.addCallback(ignoreAllArgs, reactor.stop)
    reactor.run()
