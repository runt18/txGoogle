'''
Created on 22 sep. 2014

@author: sjuul
'''
from twisted.python import log
import logging
from txGoogle.wrappers.gcd import Entity
from txGoogle.wrappers.gcd.orm.mappedProperty import MappedProperty
from txGoogle.wrappers.gcd import Key
from txGoogle.utils import simpleDeepCopy
from txGoogle.wrappers.gcd.propertyValue import PropertyValue
from txGoogle.wrappers.gcd.orm.autoStore import AutoStore
# from generic.osgoogle.osGcdWrapper import AsyncGcdWrapper


class OrmEntity(object):

    autoStoreTime = None
    autoForget = False

    def __new__(self, *args, **kwargs):
        obj = object.__new__(self, *args, **kwargs)
        obj.__class__.registerMappedProps()
        obj.__dict__['_localOrmProperties'] = {}
        obj.__dict__['_forget'] = False
        obj.__dict__['_deleted'] = False
        obj.__dict__['_changes'] = False
        if self.autoStoreTime is not None and self.autoStoreTime >= 1:
            AutoStore().addEntity(obj, self.autoStoreTime)
        return obj

    def __init__(self, entity=None, ks=None, key=None, isNew=None, *args, **kwargs):
        self._entity = self._loadEntity(entity, ks, key, isNew)
        self._copyEntValsToSelf()
        if isNew is None and isinstance(entity, dict):
            isNew = True
        if isNew:
            self._changes = True
        self._ks = ks

    def __setattr__(self, name, value):
        if name in self.__class__.ormProperties or name in self._localOrmProperties:
            if self.__dict__[name] != value:
                self.__dict__['_changes'] = True
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__class__.ormProperties or name in self._localOrmProperties:
            self.__dict__['_changes'] = True
        del self.__dict__[name]

    def hasKey(self):
        return self._entity.hasKey()

    def getKeyLen(self):
        return self._entity.getKeyLen()

    def _loadEntity(self, entity=None, ks=None, key=None, isNew=None):
        if isinstance(entity, Entity):
            ent = entity
        elif isinstance(entity, dict):
            entity = simpleDeepCopy(entity)
            if 'ks' in entity:
                if ks is not None:
                    raise Exception('Duplicate key inputs')
                ks = entity.pop('ks')
            if ks:
                if key is not None:
                    raise Exception('Duplicate key inputs')
                key = Key(ks)
            for propertyName, mapping in self.__class__.ormProperties.iteritems():
                if propertyName in entity:
                    entity[propertyName] = PropertyValue(mapping.onUnloadValue(entity[propertyName]), indexed=mapping.indexed)
            ent = Entity(entity, key=key)
        else:
            raise NotImplementedError()
        return ent

    def onUpdateFromDictOrDb(self, entity):
        self._entity = self._loadEntity(entity)
        self._copyEntValsToSelf()

    @classmethod
    def registerMappedProps(cls):
        if not hasattr(cls, 'ormProperties'):
            cls.ormProperties = {}
            for k in cls.__dict__.keys():
                v = cls.__dict__[k]
                if isinstance(v, MappedProperty):
                    cls.ormProperties[k] = v

    def _writeProperty(self, propertyName, mapping):
        value = getattr(self, propertyName)
        value = mapping.onUnloadValue(value)
        if not mapping.allowNone and value is None:
            if propertyName in self._entity:
                del self._entity[propertyName]
            return
        if self._entity.get(propertyName) != value:
            self._entity.setProperty(propertyName, value, indexed=mapping.indexed)

    def preFlush(self):
        pass

    def _updateEntityWithCurrentValues(self):
        self.preFlush()
        for propertyName, mapping in self.__class__.ormProperties.iteritems():
            self._writeProperty(propertyName, mapping)
        for propertyName, mapping in self._localOrmProperties.iteritems():
            self._writeProperty(propertyName, mapping)

    def flush(self):
        if self._changes and not self._deleted:
            self._updateEntityWithCurrentValues()
            self._changes = False

    def toDict(self):
        self._updateEntityWithCurrentValues()  # we can skip this step if we want and just construct a dict
        return self._entity.toValue()

    def _copyEntValsToSelf(self):
        handledProperties = set()
        for propertyName, workableValue in self._entity.iteritems():
            handledProperties.add(propertyName)
            if propertyName in self.__class__.ormProperties:
                mapping = self.__class__.ormProperties[propertyName]
                workableValue = mapping.onLoadValue(workableValue)
            elif propertyName not in self._localOrmProperties:
                self._localOrmProperties[propertyName] = MappedProperty(allowNone=True)
            try:
                if not hasattr(self, propertyName) or not hasattr(type(self), propertyName) or not isinstance(getattr(type(self), propertyName), property):
                    self.__dict__[propertyName] = workableValue
            except:
                log.msg('propertyName: {} propertyValue {} couldnt be set on: '.format(propertyName, workableValue, self), logLevel=logging.ERROR)
                log.err()
                raise
        propertiesLeft = set(self._localOrmProperties.keys()).union(set(self.__class__.ormProperties.keys())) - handledProperties
        for propertyName in propertiesLeft:
            if propertyName in self._localOrmProperties:
                mapping = self._localGcdPropertiess[propertyName]
            else:
                mapping = self.__class__.ormProperties[propertyName]
            if isinstance(mapping.default, (dict, list)):
                self.__dict__[propertyName] = simpleDeepCopy(mapping.default)
            else:
                self.__dict__[propertyName] = mapping.default
        self._changes = False
        self._deleted = False

    @property
    def ks(self):
        if self._ks is None:
            self._ks = self._entity.ks
            if self._ks is None:
                raise Exception('Expected a key to build Ks')
        return self._ks

    def setKey(self, key):
        self._ks = None
        self._entity.key = key

    def getKey(self):
        return self._entity.key

    def delete(self):
        self._deleted = True

    @property
    def deleted(self):
        return self._deleted

    def forget(self):
        self._entity = None
        self._forget = True

    @property
    def shouldBeForgotten(self):
        return self._forget

    @property
    def hasChanges(self):
        return self._changes

    def flushed(self):
        self._changes = False

    def __repr__(self, *args, **kwargs):
        return '{}'.format(self.__class__.__name__)

    @property
    def entity(self):
        return self._entity

    def put(self):
        self._changes = True
