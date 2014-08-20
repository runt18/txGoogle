'''
Created on 16 jul. 2014

@author: Sjuul
'''
from twisted.internet.defer import DeferredList
from twisted.internet.defer import succeed
from twisted.internet.defer import Deferred
import json
import types


def trueCb(dummy):
    return True


def falseCb(dummy):
    return False


def printCb(result, *args, **kwargs):
    if isinstance(result, types.GeneratorType):
        for item in result:
            print item
    elif result is not None:
        print json.dumps(result, indent=2)


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
