'''
Created on Oct 21, 2014

@author: sjuul
'''
from twisted.trial import unittest
from txGoogle.wrappers.gcd import Key
from txGoogle.wrappers.gcd import Entity
from txGoogle.wrappers.gcd import QueryFilter
from txGoogle.wrappers.gcd import setGlobalGcdServiceAndProjectId
from txGoogle.asyncUtils import printCb
from txGoogle.sharedConnection import SharedConnection
from txGoogle.wrappers.datastore import DatastoreWrapper
from twisted.internet.defer import inlineCallbacks
import simplejson as json


class TestGcd(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        conn = SharedConnection('785509043543.apps.googleusercontent.com', 'Mhx2IjJLk78U9VyErHHIVbnw', 'apiFiles/GcdCredentials.json')
        gcd = DatastoreWrapper(conn, projectId='over-sight')
        conn.connect()
        # getEntities(kind='Host', keysOnly=True, parentCore_eq=coreUuid)
        setGlobalGcdServiceAndProjectId(gcd, 'over-sight')

    def test_urlSafe(self):
        ks1 = 'agxzfm92ZXItc2lnaHRyJgsSCEN1c3RvbWVyIghzeXNhZG1pbgwLEglDb25kaXRpb24Ylk4M'
        key1 = Key(ks1)
        self.assert_(len(key1) == 2)
        self.assertEqual(key1.ks, ks1)

    @inlineCallbacks
    def xtest_Key_getDescendants(self):
        key = Key('Customer', 'e6b3265a8031')
        hosts = yield key.getDescendants('Host')
        self.assert_(len(hosts) > 0, 'Expected hosts')

    @inlineCallbacks
    def xtest_Key_get(self):
        key = Key('Customer', 'e6b3265a8031')
        cust = yield key.get()
        self.assertIsInstance(cust, Entity, 'Expected Customer')

    @inlineCallbacks
    def xtest_KeyWithId_get(self):
        key = Key('Customer', 'sysadmin', 'Label', 5)
        lbl = yield key.get()
        self.assertIsInstance(lbl, Entity, 'Expected Label')

    @inlineCallbacks
    def xtest_Key_exists(self):
        key = Key('Customer', 'e6b3265a8031')
        bl = yield key.exists()
        self.assertTrue(bl, 'Expected Customer to exists')

    def xtest_reserialize_entity(self):
        dct = {"properties": {"modifiedTs": {"integerValue": "1397481452"}, "conditions": {"listValue": [{"keyValue": {"path": [{"kind": "Customer", "name": "sysadmin"}, {"kind": "Condition", "id": "10006"}]}}, {"keyValue": {"path": [{"kind": "Customer", "name": "sysadmin"}, {"kind": "Condition", "id": "70002"}]}}, {"keyValue": {"path": [{"kind": "Customer", "name": "sysadmin"}, {"kind": "Condition", "id": "20004"}]}}]}, "name": {"stringValue": "copy"}, "createdTs": {"integerValue": "1397481443"}, "description": {"indexed": False, "stringValue": "Label with default conditions for the Native probe. Default label designed by Insign.it"}}, "key": {"path": [{"kind": "Customer", "name": "01fee69e075f"}, {"kind": "Label", "id": "220004"}]}}
        entity = Entity(dct, fromSerialized=True)
        serDct = entity.serialize()
        #self.assertEqual(dct, serDct, 'reserialization fails')
        original = json.dumps(dct, indent=4, sort_keys=True)
        output = json.dumps(serDct, indent=4, sort_keys=True)
        self.assertEqual(original, output, 'reserialization fails')

    def _failEb(self, fail):
        self.assert_(False, 'Exception raised: {}'.format(fail))

    @inlineCallbacks
    def xtest_load_and_write_entity(self):
        key = Key('Customer', '01fee69e075f', 'Label', 220004)
        ent = yield key.get()
        self.assertIsInstance(ent, Entity, 'Expected Label')
        dfd = ent.put()
        dfd.addErrback(self._failEb)
        wait = yield dfd
        ent2 = yield key.get()
        for propName, value in ent.iteritems():
            if isinstance(value, list):
                self.assertLessEqual(value, ent2[propName], 'Entities differ')
            else:
                self.assertEqual(value, ent2[propName], 'Entities differ')
