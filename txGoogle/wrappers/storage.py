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
from txGoogle.utils import preparePathForFile


class ObjectsWrapper(Objects):

    def _download(self, fileKey, destPath, destParentFolder):
        if 'mediaLink' in fileKey:
            if destPath:
                fileName = fileKey['id']
            else:
                fileName = os.path.join(destParentFolder, fileKey['id'])
            requestParams = {
                'url': fileKey['mediaLink'],
                'method': 'GET',
                'resultType': 'File'
            }
            dfd = self._request(requestParams)
            dfd.addCallback(self._saveFile, fileName)
        else:
            return fileKey

    def _saveFile(self, data, fileName):
        preparePathForFile(fileName)
        fl = open(fileName, 'w')
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


class StorageWrapper(Storage):

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Storage, self).__init__(conn, *args, **kwargs)
        self.defaultObjectAccessControls = DefaultObjectAccessControls(conn, *args, **kwargs)
        self.bucketAccessControls = BucketAccessControls(conn, *args, **kwargs)
        self.channels = Channels(conn, *args, **kwargs)
        self.objects = ObjectsWrapper(conn, *args, **kwargs)
        self.objectAccessControls = ObjectAccessControls(conn, *args, **kwargs)
        self.buckets = Buckets(conn, *args, **kwargs)


if __name__ == '__main__':
    from txGoogle.sharedConnection import SharedConnection
    from txGoogle.asyncUtils import printCb
    from twisted.python import log
    import sys
    from twisted.internet import reactor
    log.startLogging(sys.stdout)
    conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
    gcs = StorageWrapper(conn=conn)
    conn.connect()
    dfd = gcs.objects.download(bucket='oversight', object='23eb8fd09fbc/23eb8fd09fbc-4af16e1c97bb/matryoshkaProbe/20141003083307/7.3.2/body.msg', destPath='C:\\tmpSjj\\tmp.txt')

    @dfd.addCallback
    def onData(data):
        print data
        print 'here'

    dfd.addErrback(printCb)

    reactor.run()
