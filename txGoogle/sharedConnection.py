'''
Created on Nov 4, 2014

@author: sjuul
'''
from twisted.internet import reactor
import time
from twisted.internet.error import TimeoutError
from twisted.python import log
from twisted.internet.task import LoopingCall
from twisted.internet.defer import Deferred
from txGoogle.asyncUtils import waitTime
from txGoogle.asyncUtils import ignoreFirstArg


class SharedConnection(object):

    MAX_CONCURRENT_QUERIES = 20 - 3 # subtracting 3 because I saw connection closings when doing multiple requests
    REQUEST_RESEND_CHECK_INTERVAL = 0.06

    def __init__(self):
        self._runningReqs = []
        self._connHandler = None
        self._checkLoop = LoopingCall(self._checkTodos)
        self._checkLoop.start(self.REQUEST_RESEND_CHECK_INTERVAL, now=False)
        self._todos = []
        self._emptyQueueDfd = None

    def waitForEmptyQueue(self):
        if self._emptyQueueDfd is None:
            # make sure we wait long enough for the queue to fill
            dfd = waitTime(self.REQUEST_RESEND_CHECK_INTERVAL * 2)
            dfd.addCallback(ignoreFirstArg, self._createEmptyQueueDfd)
            return dfd
        return self._emptyQueueDfd

    def _createEmptyQueueDfd(self):
        if self._emptyQueueDfd is None:
            self._emptyQueueDfd = Deferred()
        return self._emptyQueueDfd

    def request(self, requestObj, responseHandler):
        if self._connHandler is None:
            self.connect()
        if len(self._runningReqs) < self.MAX_CONCURRENT_QUERIES:
            dfdRequest = self._connHandler.request(requestObj)
            self._runningReqs.append(requestObj)
            dfdRequest.addCallback(self._handleResponse, requestObj, responseHandler)
            dfdRequest.addErrback(self._handleFailed, requestObj, responseHandler)
        else:
            self._todos.append((requestObj, responseHandler))
        return responseHandler.dfd

    def _checkTodos(self):
        hundredSecsAgo = time.time() - 100
        for req in list(self._runningReqs):
            if req._startTs < hundredSecsAgo:
                try:
                    if not req._dfd.called:
                        self._runningReqs.remove(req)
                        req._dfd.errback(TimeoutError())
                except:
                    log.err()
            else:
                break # no use continueing because items are appended in order
        if self._todos:
            roomLeft = self.MAX_CONCURRENT_QUERIES - len(self._runningReqs)
            for _ in range(roomLeft):
                if self._todos:
                    requestObj, responseHandler = self._todos.pop(0)
                    dfdRequest = self._connHandler.request(requestObj)
                    self._runningReqs.append(requestObj)
                    dfdRequest.addCallback(self._handleResponse, requestObj, responseHandler)
                    dfdRequest.addErrback(self._handleFailed, requestObj, responseHandler)
                else:
                    break
        else:
            if self._emptyQueueDfd is not None and not self._runningReqs:
                self._emptyQueueDfd.callback('Empty')
                self._emptyQueueDfd = None

    def _handleResponse(self, response, requestObj, responseHandler):
        responseHandler.onResponse(response, requestObj)
        try:
            self._runningReqs.remove(requestObj)
        except:
            pass

    def _handleFailed(self, faillure, requestObj, responseHandler):
        responseHandler.onFailed(faillure, requestObj)
        try:
            self._runningReqs.remove(requestObj)
        except:
            pass
