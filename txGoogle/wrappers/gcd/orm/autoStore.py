'''
Created on Oct 20, 2014

@author: sjuul
'''
from generic.singleton import Singleton
from generic.loopHandler import LoopHandler
from twisted.python import log
import logging
from generic.osgoogle.osGcdWrapper import OsGcdWrapper
from txGoogle.wrappers.gcd.orm import isOrmEntity


class AutoStore(object):
    __metaclass__ = Singleton

    def __init__(self):
        self._registeredEntities = {}
        self._loopHanler = LoopHandler(self._checkChanges, interval=1)
        self._loopHanler.start(now=False)
        self._agcdW = OsGcdWrapper()

    def addEntity(self, entity, saveTime):
        assert isOrmEntity(entity)
        assert isinstance(saveTime, int)
        if entity in self._registeredEntities:
            log.msg('Doubly added entity in autoStore', logLevel=logging.WARNING)
        self._registeredEntities[entity] = saveTime

    def _checkChanges(self):
        for ent in self._registeredEntities.keys():
            if ent.shouldBeForgotten:
                del self._registeredEntities[ent]
            elif ent.deleted:
                loopTime = self._registeredEntities[ent]
                if not ent.hasKey():
                    raise Exception('Key required on entity when saving to datastore')
                self._agcdW.batchOperations.delete(ent.key, loopTime)
                self._registeredEntities.remove(ent)
            elif ent.hasChanges:
                try:
                    ent.flush()
                    loopTime = self._registeredEntities[ent]
                    self._agcdW.batchOperations.upsert(ent.entity, loopTime)
                    if ent.autoForget:
                        del self._registeredEntities[ent]
                except:
                    log.err()
                    log.msg('Removing entity from autoStore so that we dont keep looping')
                    del self._registeredEntities[ent]

    def stop(self):
        if self._loopHanler.isRunning():
            self._loopHanler.stop()
