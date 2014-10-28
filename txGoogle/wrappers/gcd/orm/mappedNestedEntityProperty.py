'''
Created on Oct 20, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcd.orm import MappedProperty
from txGoogle.wrappers.gcd.orm import OrmEntity
from txGoogle.wrappers.gcd.propertyValue import PropertyValue
#from txGoogle.wrappers.gcd import makeSureIsEntity


class MappedNestedEntityProperty(MappedProperty):

    def __init__(self, mappedClass=None, allowNone=True, default=None, repeated=False, indexed=None):
        self.mappedClass = mappedClass
        super(MappedNestedEntityProperty, self).__init__(allowNone, default, repeated, indexed)

    def onLoadItem(self, value):
        if isinstance(value, PropertyValue):
            value = value.toValue()
        if self.mappedClass is not None:
            return self.mappedClass(value)
        else:
            return OrmEntity(value)

    def onUnloadItem(self, value):
        if isinstance(value, OrmEntity):
            return value.entity
        else:
            raise Exception('Unexpected value')
        #return makeSureIsEntity(value)
