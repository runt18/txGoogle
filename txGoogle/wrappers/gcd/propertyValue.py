'''
Created on Oct 21, 2014

@author: sjuul
'''
from txGoogle.timeUtils import timestampToDateTime
from txGoogle.timeUtils import datetimeToTimestamp
import base64
from txGoogle.wrappers.gcd import determineValueKind
from txGoogle.wrappers.gcd import makeSureIsPropertyValue
from txGoogle.wrappers.gcd import makeSureIsKey
from txGoogle.wrappers.gcd import buildEntity
from txGoogle.wrappers.gcd import unpackSerializedPropertyValues
from txGoogle.wrappers.gcd import SerializationException


class PropertyValue(object):

    def __init__(self, value, valueKind=None, indexed=None, fromSerialized=False):
        self.indexed = indexed
        if valueKind is None:
            self.valueKind, value = determineValueKind(value)
        else:
            self.valueKind = valueKind
        if self.valueKind == 'dateTimeValue':
            value = timestampToDateTime(value / 1000000)
        elif self.valueKind == 'entityValue':
            value = buildEntity(value, fromSerialized=fromSerialized)
        elif self.valueKind == 'listValue':
            if fromSerialized:
                value = list(unpackSerializedPropertyValues(value, fromSerialized=fromSerialized))
            else:
                value = [makeSureIsPropertyValue(vl) for vl in value]
        elif self.valueKind == 'keyValue':
            value = makeSureIsKey(value)
        elif self.valueKind == 'blobValue':
            if fromSerialized:
                mod = len(value) % 4
                if mod:
                    value += '=' * (4 - mod)
                value = base64.decodestring(value.replace('-', '+').replace('_', '/'))
        self.value = value

    def toValue(self):
        if self.valueKind == 'entityValue':
            return self.value.toValue()
        elif self.valueKind == 'listValue':
            return [vl.toValue() for vl in self.value]
        elif self.valueKind == 'keyValue':
            return self.value.ks
        else:
            return self.value

    def serialize(self):
        if self.valueKind == 'blobValue':
            value = base64.encodestring(self.value).replace('+', '-').replace('/', '_').strip().rstrip('=')
        elif self.valueKind == 'entityValue':
            value = self.value.serialize(outputKey=False)
        elif self.valueKind == 'listValue':
            if self.value:
                value = [item.serialize() for item in self.value]
            else:
                value = None
        elif self.valueKind == 'dateTimeValue':
            value = datetimeToTimestamp(value) * 1000000
        elif self.valueKind == 'keyValue':
            value = self.value.serialize()
        else:
            value = self.value
        output = {}
        if self.indexed is not None:
            output['indexed'] = self.indexed
        if value is not None:
            output[self.valueKind] = value
        return output

    def __repr__(self):
        return str(self.value)
