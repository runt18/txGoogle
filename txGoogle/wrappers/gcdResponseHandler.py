'''
Created on Oct 17, 2014

@author: sjuul
'''
from txGoogle.googleResponseHandler import GoogleResponseHandler
from txGoogle.asyncUtils import loggedException
from txGoogle.wrappers.gcd import Entity
from txGoogle.wrappers.gcd import Key
from twisted.python import log
import logging


class GcdResponseHandler(GoogleResponseHandler):

    @loggedException
    def _loadValues(self, valueDcts):
        for dct in valueDcts:
            if 'entity' in dct:
                yield Entity(dct['entity'], fromSerialized=True)
            if 'key' in dct:
                yield Key(dct['key'])

    def _loadResults_LookupResponse(self, loaded):
        if self._result is None:
            self._result = {'found': [], 'deferred': [], 'missing': []}
        if loaded['found']:
            self._result['found'].extend(self._loadValues(loaded['found']))
        if loaded['deferred']:
            self._result['deferred'].extend(self._loadValues(loaded['deferred']))
        if loaded['missing']:
            self._result['missing'].extend(self._loadValues(loaded['missing']))
            
    def _loadResults_RunQueryResponse(self, loaded):
        if self._result is None:
            self._result = []
        batchRes = loaded.get('batch', {})
        self._result.extend(self._loadValues(batchRes.get('entityResults', [])))
        self._result.extend(self._loadValues(batchRes.get('keyResults', [])))
        if batchRes.get('skippedResults'):
            log.msg('Skipped Results found', logLevel=logging.WARNING)

