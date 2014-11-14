'''
Created on 3 okt. 2014

@author: sjuul
'''
from txGoogle.services.storage_ import Storage
from txGoogle.services.storage_ import BucketAccessControls
from txGoogle.services.storage_ import Channels
from txGoogle.services.storage_ import Objects
from txGoogle.services.storage_ import ObjectAccessControls
from txGoogle.services.storage_ import Buckets
from txGoogle.services.storage_ import DefaultObjectAccessControls
import os
from txGoogle.utils import preparePathForFile, getFilesInFolder
from txGoogle.wrappers.gcsResponseHandler import GcsResponseHandler
from txGoogle.asyncUtils import mapFunToItems
from twisted.internet.defer import DeferredList
from twisted.python import log
import logging


class ObjectsWrapper(Objects):

    def _download(self, fileKey, destPath, destParentFolder):
        if 'mediaLink' in fileKey:
            if destPath:
                fileName = destPath
            else:
                fileName = os.path.join(destParentFolder, fileKey['name'])
            requestParams = {
                'url': fileKey['mediaLink'],
                'method': 'GET',
                'resultType': 'File'
            }
            dfd = self._request(requestParams)
            dfd.addCallback(self._saveFile, fileName)
            return dfd
        else:
            return fileKey

    def _saveFile(self, data, fileName):
        preparePathForFile(fileName)
        fl = open(fileName, 'wb')
        fl.write(data)
        fl.close()

    def download(self, object, bucket, destPath=None, destParentFolder=None, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, ifGenerationNotMatch=None, generation=None, ifMetagenerationMatch=None, ifGenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
        if destPath is not None and destParentFolder is not None:
            raise Exception('Either use despath or destParentFolder, not both')
        if destPath is None and destParentFolder is None:
            raise Exception('Either use despath or destParentFolder')
        dfd = self.get(object, bucket, prettyPrint, fields, quotaUser, oauth_token, key, userIp, alt, ifGenerationNotMatch, generation, ifMetagenerationMatch, ifGenerationMatch, ifMetagenerationNotMatch, projection)
        dfd.addCallback(self._download, destPath, destParentFolder)
        return dfd

    def emptyFolder(self, bucket, path):
        dfdL = self.list(bucket=bucket, prefix=path)
        dfdL.addCallback(self._extractFileNames)
        dfdL.addCallback(mapFunToItems, self.delete, bucket=bucket)
        return dfdL

    def _extractFileNames(self, res):
        files = res.get('items', [])
        return [fileItem['name'] for fileItem in files]

    def syncFolder(self, bucket, gcsFolderName, localPath, direction, stripLocalExtension=None):
        assert direction in ('down', 'up', 'both')
        dfd = self.list(bucket=bucket, prefix=gcsFolderName)
        dfd.addCallback(self._onFilesToSync, gcsFolderName, localPath, direction, stripLocalExtension)
        return dfd

    def _onFilesToSync(self, gcsFiles, gcsFolderName, localPath, direction, stripLocalExtension):
        dfds = []
        localFiles = getFilesInFolder(localPath, minFileSize=100, stripExtension=stripLocalExtension)
        if direction in ('down', 'both'):
            localFilesIdx = set(localFiles)
            for item in gcsFiles['items']:
                relName = os.path.relpath(item['name'], gcsFolderName)
                if relName not in localFilesIdx:
                    msg = 'Downloading {}'.format(relName)
                    print msg
                    log.msg(msg, logLevel=logging.INFO)
                    destPath = os.path.join(localPath, relName)
                    dfds.append(self._download(item, destPath, None))
        if direction in ('up', 'both'):
            raise NotImplementedError()
        return DeferredList(dfds)


class StorageWrapper(Storage):

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        kwargs['responseCls'] = GcsResponseHandler
        conn.registerScopes(self._scopes)
        super(StorageWrapper, self).__init__(conn, *args, **kwargs)
        self.objects = ObjectsWrapper(self, conn, *args, **kwargs)


if __name__ == '__main__':
    from txGoogle.sharedOauthConnection import SharedOauthConnection
    from txGoogle.asyncUtils import printCb
    import sys
    from twisted.internet import reactor
    log.startLogging(sys.stdout)
    conn = SharedOauthConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
    gcs = StorageWrapper(conn=conn)
    conn.connect()
    dfd = gcs.objects.list(bucket='oversight', prefix='23eb8fd09fbc/23eb8fd09fbc-007f7d813bb6/')
    #dfd = gcs.objects.download(bucket='oversight', object='23eb8fd09fbc/23eb8fd09fbc-4af16e1c97bb/matryoshkaProbe/20141003083307/7.3.2/body.msg', destPath='C:\\tmpSjj\\tmp.txt')

    @dfd.addCallback
    def onData(data):
        print data
        print 'here'

    dfd.addErrback(printCb)

    reactor.run()
