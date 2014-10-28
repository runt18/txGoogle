'''
Created on Oct 20, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcd.orm import MappedProperty
from txGoogle.wrappers.gcd import makeSureIsKey
from txGoogle.wrappers.gcd import Key


class MappedKsKeyProperty(MappedProperty):

    def onLoadItem(self, value):
        if isinstance(value, basestring):
            return value
        elif isinstance(value, Key):
            return value.ls
        else:
            raise Exception('Unexpected value')

    def onUnloadItem(self, value):
        return makeSureIsKey(value)
