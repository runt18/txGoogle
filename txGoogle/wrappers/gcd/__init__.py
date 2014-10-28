import datetime


class GcdObjectWithApiBackReference(object):

    _globalGcdWrapper = None
    _defaultProjectId = None

    @classmethod
    def setDefaultGcdWrapper(cls, globalGcdWrapper, defaultProjectId):
        cls._globalGcdWrapper = globalGcdWrapper
        cls._defaultProjectId = defaultProjectId


def enumerateKeypairs(keypairs):
    itr = iter(keypairs)
    for kind in itr:
        idName = next(itr)
        yield kind, idName


def buildValueDct(value):
    valueKind, outValue = determineValueKind(value)
    if valueKind in ('entityValue', 'keyValue'):
        outValue = trySerialize(outValue)
    return {valueKind: outValue}


def unpackSerializedPropertyValues(values, fromSerialized):
    assert fromSerialized == True, 'dont know if needed'
    for value in values:
        firstKey = next(iter(value))
        yield PropertyValue(value[firstKey], firstKey, fromSerialized=fromSerialized)


def determineValueKind(value):
    if isinstance(value, basestring):
        if len(value) > 500:
            valueKind = 'blobValue'
        else:
            try:  # http://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
                value = value.decode('ascii')
                valueKind = 'stringValue'
            except:
                valueKind = 'blobValue'
    elif isinstance(value, bool):
        valueKind = 'booleanValue'
    elif isinstance(value, int):
        valueKind = 'integerValue'
    elif isinstance(value, long):
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
    elif isinstance(value, Entity):
        valueKind = 'entityValue'
    else:
        value = None
        raise Exception('Not supported: ' + str(type(value)))
    return valueKind, value


def makeSureIsKey(value):
    if not isinstance(value, Key):
        return Key(value)
    return value


def makeSureIsEntity(value):
    if not isinstance(value, Entity):
        return Entity(value)
    return value


def makeSureIsPropertyValue(value):
    if not isinstance(value, PropertyValue):
        return PropertyValue(value)
    return value


def buildEntity(*args, **kwargs):
    return Entity(*args, **kwargs)


def setGlobalGcdServiceAndProjectId(gcdService, projectId):
    GcdObjectWithApiBackReference.setDefaultGcdWrapper(gcdService, projectId)


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


from pathPart import PathPart
from queryFilter import QueryFilter
from key import Key
from propertyValue import PropertyValue
from entity import Entity
