'''
Created on 15 okt. 2014

@author: Sjuul
'''
import datetime
from txGoogle.timeUtils import datetimeToTimestamp, timestampToDateTime
from txGoogle.wrappers.gcdKeyNdbKey import urlSafeFromPairs, getPairsFromUrlSafe
import base64
from txGoogle.asyncUtils import hasListItems
from twisted.python import log


def trySerialize(obj):
    if isinstance(obj, basestring):
        return Key(obj).serialize()
    if hasattr(obj, 'serialize'):
        return obj.serialize()
    else:
        return obj

def checkKindsFormat(kind):
    if isinstance(kind, basestring):
        return {'name': kind}
    elif isinstance(kind, dict):
        if 'name' not in kind:
            raise Exception('Expected name field in Kind')
        return kind


def enumerateKeypairs(keypairs):
    itr = iter(keypairs)
    for kind in itr:
        idName = next(itr)
        yield kind, idName


class GcdObjectWithApiBackReference(object):

    _globalGcdWrapper = None
    _defaultProjectId = None

    @classmethod
    def setDefaultGcdWrapper(cls, globalGcdWrapper, defaultProjectId):
        cls._globalGcdWrapper = globalGcdWrapper
        cls._defaultProjectId = defaultProjectId


def setGlobalGcdServiceAndProjectId(gcdService, projectId):
    GcdObjectWithApiBackReference.setDefaultGcdWrapper(gcdService, projectId)


class PathPart(object):

    def __init__(self, kind, name=None, id=None):
        self.kind = kind
        self.name = name
        if id:
            id = long(id)
        self.id = id

    def serialize(self):
        if self.name:
            return {'kind': self.kind, 'name': self.name}
        else:
            return {'kind': self.kind, 'name': self.name}

    def nameId(self):
        if self.name:
            return self.name
        else:
            return self.id

class Key(GcdObjectWithApiBackReference):

    def __init__(self, *inpTup):
        self.partitionId = {}
        if len(inpTup) == 1:
            inp = inpTup[0]
            if isinstance(inp, basestring):
                self._fromPairs(getPairsFromUrlSafe(inp))
            elif isinstance(inp, dict):
                self.path = [PathPart(**part) for part in inp.get('path', [])]
                self.partitionId = inp.get('partitionId', {})
            elif isinstance(inp, list):
                self.path = inp
            else:
                raise Exception('unknown key instantiation')
        else:
            return self._fromPairs(enumerateKeypairs(inpTup))
                
    def getLen(self):
        return len(self.path)
        
    def _fromPairs(self, pairs):
        self.path = []
        for kind, idName in pairs:
            if isinstance(idName, basestring):
                self.path.append(PathPart(kind, name=idName))
            else:
                self.path.append(PathPart(kind, id=idName))
        
        
    @property
    def datasetId(self):
        dsId = self.partitionId.get('datasetId')
        if dsId:
            dsId = dsId.split('~')[-1]
        return dsId

    def serialize(self):
        print [(elem.kind, elem.nameId()) for elem in self.path]
        return {
            # 'key': {
                'path': [elem.serialize() for elem in self.path]
            # }
        }
        
    def getPairs(self):
        for elem in self.path:
            yield elem.kind, elem.nameId()
            
    def getParentName(self, parentName):
        for elem in self.path:
            if elem.name == parentName:
                return elem.name
        
    @property
    def ks(self):
        return urlSafeFromPairs(self.datasetId or self._defaultProjectId, self.getPairs())
    
    def toDict(self):
        assert 0
        print self
        
    def exists(self):
        dfd = self._globalGcdWrapper.datasets.query(self.datasetId or self._defaultProjectId, queryFilter=QueryFilter().keyEquals(self), properties=['__key__'])
        dfd.addCallback(hasListItems)
        dfd.addErrback(log.err)
        return dfd

    def getDescendants(self, kind, keysOnly=False):
        if keysOnly:
            properties = ['__key__']
        else:
            properties = None
        dfd = self._globalGcdWrapper.datasets.query(self.datasetId or self._defaultProjectId, queryFilter=QueryFilter().hasAncestor(self), properties=properties)
        dfd.addCallback(hasListItems)
        dfd.addErrback(log.err)
        return dfd
        pass


def determineValueKind(value):
    if isinstance(value, basestring):
        if len(value) > 500:
            valueKind = 'blobValue'
        else:
            valueKind = 'stringValue'
    elif isinstance(value, bool):
        valueKind = 'booleanValue'
    elif isinstance(value, int):
        valueKind = 'integerValue'
    elif isinstance(value, float):
        valueKind = 'doubleValue'
    elif isinstance(value, datetime.datetime):
        valueKind = 'dateTimeValue'
    elif isinstance(value, dict):
        if 'keyValue' in value:
            valueKind = 'keyValue'
            value = value['keyValue']
        else:
            valueKind = 'entityValue'
    elif isinstance(value, list):
        valueKind = 'listValue'
        value = [PropertyValue(vl) for vl in value]
    elif isinstance(value, Key):
        valueKind = 'keyValue'
    else:
        value = None
        raise Exception('Not supported: ' + str(type(value)))
    return valueKind, value

def buildValueDct(value):
    valueKind, outValue = determineValueKind(value)
    return {valueKind: trySerialize(outValue)}


def unpackSerializedPropertyValues(values, fromSerialized):
    assert fromSerialized == True, 'dont know if needed'
    for value in values:
        firstKey = next(iter(value))
        yield PropertyValue(value[firstKey], firstKey, fromSerialized=fromSerialized).value


class PropertyValue(object):

    def __init__(self, value, valueKind=None, indexed=False, fromSerialized=False):
        self.indexed = indexed
        if valueKind is None:
            self.valueKind, value = determineValueKind(value)
        else:
            self.valueKind = valueKind
        if self.valueKind == 'dateTimeValue':
            value = timestampToDateTime(value / 1000000)
        elif self.valueKind == 'entityValue':
            value = Entity(value, fromSerialized=fromSerialized)
        elif self.valueKind == 'listValue':
            if fromSerialized:
                value = list(unpackSerializedPropertyValues(value, fromSerialized=fromSerialized))
            else:
                value = [vl for vl in value]
        elif self.valueKind == 'keyValue':
            value = Key(value)
        elif self.valueKind == 'blobValue':
            mod = len(value) % 4
            if mod:
                value += '=' * (4 - mod)
            value = base64.decodestring(value.replace('-', '+').replace('_', '/'))

        self.value = value

    def toDict(self):
        if self.valueKind == 'entityValue':
            return self.value.toDict()
        elif self.valueKind == 'listValue':
            output = []
            for vl in self.value:
                if hasattr(vl, 'toDict'):
                    output.append(vl.toDict())
                else:
                    output.append(vl)
            return output
        else:
            return self.value

    def serialize(self):
        if self.valueKind == 'blobValue':
            value = base64.encodestring(self.value).replace('+', '-').replace('/', '_').rstrip(['='])
        elif self.valueKind == 'entityValue':
            value = value.serialize(outputKey=False)
        elif self.valueKind == 'listValue':
            value = [item.serialize() for item in self.value]
        elif self.valueKind == 'dateTimeValue':
            value = datetimeToTimestamp(value) * 1000000
        else:
            value = self.value
        return {self.valueKind: value}


class Entity(GcdObjectWithApiBackReference):

    def __init__(self, dct=None, fromSerialized=False, key=None):
        self.key = None
        if dct is None:
            dct = {}
        self.properties = {}
        if fromSerialized:
            if not 'properties' in dct:
                print '???'
            for ky, vl in dct['properties'].iteritems():
                if ky == 'probes':
                    print vl
                if 'indexed' in vl:
                    del vl['indexed']
                    indexed = True
                else:
                    indexed = False
                if vl:
                    firstKey = next(iter(vl))
                    self.properties[ky] = PropertyValue(vl[firstKey], valueKind=firstKey, indexed=indexed, fromSerialized=fromSerialized)
                else:
                    self.properties[ky] = PropertyValue(None, valueKind='None', indexed=False, fromSerialized=fromSerialized)
            if 'key' in dct:
                self.key = Key(dct['key'])
        else:
            if 'ks' in dct:
                self.key = Key(dct.pop('ks'))
            for ky, vl in dct.iteritems():
                self.properties[ky] = PropertyValue(vl, valueKind=None, indexed=True, fromSerialized=fromSerialized)
        if key:
            self.key = key

    @property
    def kind(self):
        if self.key.path:
            return self.key.path[-1].kind

    @property
    def name(self):
        if self.key.path:
            return self.key.path[-1].name

    def toDict(self):
        return {ky: vl.toDict() for ky, vl in self.properties.iteritems()}

    def __getitem__(self, key):
        val = self.properties.get(key)
        if val is None:
            return None
        return val.value

    def iteritems(self):
        for ky, vl in self.properties.iteritems():
            yield ky, vl.value

    def __setitem__(self, key, value):
        return self.setProperty(key, value)

    def setProperty(self, key, value, valueKind=None, indexed=True):
        self.properties[key] = PropertyValue(value, indexed=indexed)

    def getProperty(self, key, default=None):
        if key in self.properties:
            return self.properties[key].value
        else:
            return default

    get = getProperty

    def __contains__(self, key):
        return key in self.properties

    def serialize(self, outputKey=True):
        properties = {}
        output = {
            'properties': properties
        }
        if outputKey:
            output['key'] = self.key.serialize()
        for prop in self.property:
            properties[prop.name] = prop.serialize()
            if not prop.indexed:
                properties[prop.name]['indexed'] = False
        return output

    def getKeyLen(self):
        if self.key:
            return self.key.getLen()
        return 0

    def hasKey(self):
        if not self.key:
            return False
        return self.key.getLen() > 0
    
    def __str__(self, *args, **kwargs):
        return str(self.toDict())

    def __repr__(self, *args, **kwargs):
        return str(self.toDict())

    @property
    def ks(self):
        if self.key:
            return self.key.ks

class QueryFilter(object):
    
    def __init__(self):
        self._filters = []
        
    def serialize(self):
        cnt = len(self._filters)
        if cnt == 0:
            return {}
        elif cnt == 1:
            return { 'propertyFilter': self._filters[0] }
        else:
            return {
                'compositeFilter': [ {'propertyFilter': fltr for fltr in self._filters } ]
            }

    def equal(self, propertyName, value):
        self._filters.append({'property': {'name': propertyName}, 'value': buildValueDct(value), 'operator': 'EQUAL'})
        return self

    def lessThan(self, propertyName, value):
        self._filters.append({'property': {'name': propertyName}, 'value': buildValueDct(value), 'operator': 'LESS_THAN'})
        return self
    
    def lessThanOrEqual(self, propertyName, value):
        self._filters.append({'property': {'name': propertyName}, 'value': buildValueDct(value), 'operator': 'LESS_THAN_OR_EQUAL'})
        return self
    
    def greaterThan(self, propertyName, value):
        self._filters.append({'property': {'name': propertyName}, 'value': buildValueDct(value), 'operator': 'GREATER_THAN'})
        return self
    
    def greaterThanOrEqual(self, propertyName, value):
        self._filters.append({'property': {'name': propertyName}, 'value': buildValueDct(value), 'operator': 'GREATER_THAN_OR_EQUAL'})
        return self
    
    def hasAncestor(self, value):
        if not isinstance(value, Key):
            value = Key(value)
        self._filters.append({'value': {'keyVale': value.serialize()}, 'operator': 'HAS_ANCESTOR'})
        return self

    def keyEquals(self, value):
        if not isinstance(value, Key):
            value = Key(value)
        self._filters.append({'value': {'keyVale': value.serialize()}, 'operator': 'EQUALS'})
        return self
