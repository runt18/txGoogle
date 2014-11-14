'''
Created on 24 okt. 2014

@author: Sjuul
'''
from twisted.trial import unittest
from txGoogle.sharedOauthConnection import SharedOauthConnection
from twisted.internet.defer import inlineCallbacks
import simplejson as json
from txGoogle.wrappers.storage import StorageWrapper


class TestGcd(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        conn = SharedOauthConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcsCredentials.json')
        self.gcs = StorageWrapper(conn)
        conn.connect()

    @inlineCallbacks
    def xtest_list_files_in_folder(self):
        items = yield self.gcs.objects.list(bucket='debug_bucket', prefix='test/')
        self.assert_(len(items['items']) > 0, 'Folder not filled?')

    def test_remove_objects_in_folder(self):
        return self.gcs.objects.emptyFolder('oversight_email', 'inprogress/matryoshkaProbe/23eb8fd09fbc/0135030877/')
