'''
Created on 15 aug. 2014

@author: sjuul
'''

from txGoogle.services.discovery import Discovery
from txGoogle.asyncBase import AsyncBase
from txGoogle.asyncUtils import printCb, mapFunToItems
import json


class DiscoveryWrapper(Discovery):
    
    def getList(self):
        return self.apis.list(preferred=True)
    
    def downloadPreferred(self, apiNames=None):
        '''Download the specified api's docs. If no apiNames are given all apiDocs are downloaded'''
        dfd = self.apis.list(preferred=True)

        #def fun(discoveryItem):
        #    self.download(discoveryItem['name'], discoveryItem['version'], 'apiFiles/apiDocs/{}.json'.format(discoveryItem['name']))
        
        #dfd.addCallback(mapFunToItems, fun)
        @dfd.addCallback
        def fun(discoveryList):
            for discoveryItem in discoveryList['items']:
                if apiNames:
                    if not discoveryItem['name'] in apiNames:
                        continue
                self.download(discoveryItem['name'], discoveryItem['version'], 'apiFiles/apiDocs/{}.json'.format(discoveryItem['name']))
        
        return dfd
    
    def download(self, apiName, version, filePath):
        dfd = self.apis.getRest('gmail', 'v1')
        print apiName
        @dfd.addCallback
        def fun(contents):
            print type(contents), filePath
            json.dump(contents, open(filePath, 'w'))
        return dfd
            

if __name__ == '__main__':
    from twisted.internet import reactor
    conn = AsyncBase('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/AsyncAllCredentials.json')
    downloader = DiscoveryWrapper(conn)
    #dfd = downloader.download('gmail', 'v1', 'apiFiles/apiDocs/gmail.json')
    #dfd = downloader.getList()
    dfd = downloader.downloadPreferred(['gmail', 'bigquery'])
    dfd.addCallback(printCb)
    reactor.run()
