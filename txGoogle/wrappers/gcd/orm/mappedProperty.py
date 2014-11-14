'''
Created on Oct 20, 2014

@author: sjuul
'''
from txGoogle.utils import simpleDeepCopy


class MappedProperty(object):

    def __init__(self, allowNone=True, default=None, repeated=False, indexed=None):
        self.allowNone = allowNone
        self._default = default
        self.repeated = repeated
        self.indexed = indexed

    @property
    def default(self):
        if self._default is not None:
            return simpleDeepCopy(self._default)
        if self.repeated:
            return []
        return None

    def onLoadValue(self, value):
        '''
        called when mapping is loaded onto self
        This handles the repeated stuff so that the other mappedProperty subclasses dont have to
        '''
        if self.repeated:
            if value is None:
                return []
            else:
                return [self.onLoadItem(item) for item in value]
        else:
            return self.onLoadItem(value)

    def onUnloadValue(self, value):
        '''
        called when mapping is put back to entity
        This handles the repeated stuff so that the other mappedProperty subclasses dont have to
        '''
        if self.repeated:
            if value is None:
                return []
            else:
                output = []
                for item in value:
                    if item is None:
                        output.append(None)
                    else:
                        output.append(self.onUnloadItem(item))
                return output
        else:
            if value is None:
                return self.default
            else:
                return self.onUnloadItem(value)

    def onLoadItem(self, value):
        return value

    def onUnloadItem(self, value):
        return value
