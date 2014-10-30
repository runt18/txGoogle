'''
Created on Oct 21, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcdKeyNdbKey import getPairsFromUrlSafe
from txGoogle.wrappers.gcdKeyNdbKey import urlSafeFromPairs
from txGoogle.wrappers.gcd import GcdObjectWithApiBackReference
from txGoogle.wrappers.gcd import enumerateKeypairs
from txGoogle.wrappers.gcd.queryFilter import QueryFilter
from txGoogle.wrappers.gcd import PathPart
from txGoogle.asyncUtils import hasItems
from txGoogle.asyncUtils import pickFirst
from twisted.python import log


class Key(GcdObjectWithApiBackReference):

    def __init__(self, *inpTup, **kwargs):
        self.partitionId = {}
        if len(inpTup) == 1:
            inp = inpTup[0]
            if isinstance(inp, basestring):
                try:
                    self._fromPairs(getPairsFromUrlSafe(inp))
                except Exception as ex:
                    print ex
            elif isinstance(inp, dict):
                self.path = [PathPart(**part) for part in inp.get('path', [])]
                self.partitionId = inp.get('partitionId', {})
            elif isinstance(inp, list):
                self.path = inp
            else:
                raise Exception('unknown key instantiation')
        else:
            self._fromPairs(enumerateKeypairs(inpTup))
        if 'ancestor' in kwargs:
            self.path = kwargs['ancestor'].path + self.path

    def getLen(self):
        raise Exception('deprecated')

    def _fromPairs(self, pairs):
        self.path = []
        encounteredNone = False
        encounteredParentNone = False
        for kind, idName in pairs:
            if encounteredNone:
                encounteredParentNone = True
            if idName is None:
                encounteredNone = True
            if isinstance(idName, basestring):
                self.path.append(PathPart(kind, name=idName))
            else:
                self.path.append(PathPart(kind, id=idName))
        if encounteredParentNone:
            pathElemStr = ', '.join([str(item) for item in self.path])
            raise Exception('One of the parents is None, this is not allowed in a Key. Path: {}'.format(pathElemStr))

    @property
    def datasetId(self):
        dsId = self.partitionId.get('datasetId')
        if dsId:
            dsId = dsId.split('~')[-1]
        return dsId

    def serialize(self):
        return {
            'path': [elem.serialize() for elem in self.path]
        }

    def getPairs(self):
        for elem in self.path:
            yield elem.kind, elem.nameId()

    def getParentName(self, parentName):
        for elem in self.path:
            if elem.kind == parentName:
                return elem.name

    def getParentNames(self, parentNames=None):
        return list(self._getParentNames(parentNames))

    def _getParentNames(self, parentNames=None):
        if parentNames is None:
            for elem in self.path:
                yield elem.nameId()
        else:
            for parentName in parentNames:
                yield self.getParentName(parentName)

    @property
    def ks(self):
        myPairs = list(self.getPairs())
        if len(myPairs) == 0:
            return None
        return urlSafeFromPairs(self.datasetId or self._defaultProjectId, myPairs)

    def toValue(self):
        return self

    def toDict(self):
        return self.ks

    def exists(self):
        dfd = self._globalGcdWrapper.datasets.query(self.datasetId or self._defaultProjectId, kinds=None, queryFilter=QueryFilter().keyEquals(self), properties=['__key__'])
        dfd.addCallback(hasItems)
        dfd.addErrback(log.err)
        return dfd

    def get(self):
        dfd = self._globalGcdWrapper.datasets.query(self.datasetId or self._defaultProjectId, kinds=None, queryFilter=QueryFilter().keyEquals(self))
        dfd.addCallback(pickFirst)
        dfd.addErrback(log.err)
        return dfd

    def getDescendants(self, kind, keysOnly=False):
        if keysOnly:
            properties = ['__key__']
        else:
            properties = None
        dfd = self._globalGcdWrapper.datasets.query(self.datasetId or self._defaultProjectId, kinds=[kind], queryFilter=QueryFilter().hasAncestor(self), properties=properties)
        dfd.addErrback(self._onErr)
        return dfd

    def _onErr(self, fail):
        log.err(fail)

    def __repr__(self):
        if self.path:
            return '(Key: ' + ', '.join(elem.__repr__() for elem in self.path) + ')'
        return 'Empty key'

    def __eq__(self, other):
        return self.path == other.path

    def __len__(self):
        return len(self.path)

    @property
    def nameId(self):
        if self.path:
            return self.path[-1].nameId

    @property
    def name(self):
        if self.path:
            return self.path[-1].name

    @property
    def id(self):
        if self.path:
            return self.path[-1].id

if __name__ == '__main__':
    print repr(Key('agpvdmVyLXNpZ2h0cgsLEgVMYWJlbBgFDA'))
