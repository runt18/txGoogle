'''
Created on Oct 20, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcd.orm import MappedProperty
import simplejson as json


class MappedJsonStringProperty(MappedProperty):

    def __init__(self, *args, **kwargs):
        super(MappedJsonStringProperty, self).__init__(*args, **kwargs)

    def onLoadItem(self, value):
        if isinstance(value, basestring):
            return json.loads(value)
        else:
            raise Exception('Unexpected value')

    def onUnloadItem(self, value):
        return json.dumps(value)
