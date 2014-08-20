'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.discovery import Discovery
from txGoogle.asyncBase import AsyncBase
from txGoogle.asyncUtils import printCb, mapFunToItems, ignoreFirstArg, \
    ignoreAllArgs
import json
import os
from txGoogle.utils import preparePathForFile
from twisted.internet.defer import DeferredList
from txGoogle.asyncApisGenerator import generateCode


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
            print 'downloaded {}'.format(apiName)
        return dfd


if __name__ == '__main__':
    from twisted.internet import reactor
    conn = AsyncBase('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', '../apiFiles/AsyncAllCredentials.json')
    downloader = DiscoveryWrapper(conn)
    conn.connect()
    serviceList = ['gmail', 'bigquery', 'storage', 'pubsub', 'cloudmonitoring', 'datastore']
    dfd = downloader.downloadPreferred(serviceList)

    dfd.addCallback(ignoreFirstArg, generateCode, serviceList)
    dfd.addCallback(ignoreAllArgs, reactor.stop)
    reactor.run()
