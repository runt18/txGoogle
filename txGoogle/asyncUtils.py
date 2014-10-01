'''
Created on 16 jul. 2014

@author: Sjuul
'''
from twisted.internet.defer import DeferredList
from twisted.internet.defer import fail
from twisted.internet.defer import succeed
from twisted.internet.defer import Deferred
import json
import types
from twisted.python import log


def trueCb(dummy):
    return True


def falseCb(dummy):
    return False


def printCb(result, *args, **kwargs):
    if isinstance(result, types.GeneratorType):
        for item in result:
            print item
    elif result is not None:
        try:
            print json.dumps(result, indent=2)
        except:
            print result


def mapFunToItems(items, fun, *args, **kwargs):
    results = []
    for item in items:
        funRes = fun(item, *args, **kwargs)
        results.append(funRes)
    if results and isinstance(results[0], Deferred):
        return DeferredList(results)
    else:
        return succeed(results)


def mapFunToItemsSequentially(items, fun, *args, **kwargs):
    results = []
    for item in items:
        print item
        print fun, args, kwargs
        funRes = fun(item, *args, **kwargs)
        results.append(funRes)
    return results


def addPrintCbs(dfds):
    for df in dfds:
        df.addCallback(printCb)
        df.addErrback(printCb)


def ignoreFirstArg(dummy, fun, *args, **kwargs):
    return fun(*args, **kwargs)


def ignoreAllArgs(dummy, fun, *args, **kwargs):
    return fun()


def wrapCallback(fun, cb):
    def wrapper(*args, **kwargs):
        dfd = fun(*args, **kwargs)
        if isinstance(dfd, Deferred):
            dfd.addCallback(cb)
        return dfd
    return wrapper


class immutableKwargs(dict):
    '''
    Only useable if kwargs don't change!!!
    '''
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def __setitem__(self, *args, **kwargs):
        raise Exception('not allowed')

    def __delitem__(self, *args, **kwargs):
        raise Exception('not allowed')


def cacheDfdWhileRunning(fun):

    def clearCacheCb(result, key):
        del fun.dfds[key]
        return result

    def clearCacheEb(result, key):
        del fun.dfds[key]
        return fail(result)

    def wrapper(*args, **kwargs):
        if not hasattr(fun, 'dfds'):
            fun.dfds = {}
        key = (args, immutableKwargs(kwargs))
        if key in fun.dfds:
            return fun.dfds[key]
        else:
            result = fun(*args, **kwargs)
            if isinstance(result, Deferred) and not result.called:
                fun.dfds[key] = result
                result.addCallback(clearCacheCb, key=key)
                result.addErrback(clearCacheEb, key=key)
            return result

    return wrapper

def loggedException(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            log.err()
    return wrapper


