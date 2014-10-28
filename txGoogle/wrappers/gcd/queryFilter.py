'''
Created on Oct 21, 2014

@author: sjuul
'''
from txGoogle.wrappers.gcd import buildValueDct, makeSureIsKey


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
        value = makeSureIsKey(value)
        self._filters.append({'property': {'name': '__key__'}, 'value': {'keyValue': value.serialize()}, 'operator': 'HAS_ANCESTOR'})
        return self

    def keyEquals(self, value):
        value = makeSureIsKey(value)
        self._filters.append({'property': {'name': '__key__'}, 'value': {'keyValue': value.serialize()}, 'operator': 'EQUAL'})
        return self
