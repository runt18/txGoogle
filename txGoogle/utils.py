'''
Created on 15 aug. 2014

@author: sjuul
'''
import os


def dictGet(dct, keys, default):
    for key in keys[:-1]:
        if key in dct:
            dct = dct[key]
        else:
            return default
    if keys[-1] in dct:
        return dct[keys[-1]]
    else:
        return default


def leaveOutNulls(dct):
    for a, b in dct.items():
        if isinstance(b, dict):
            leaveOutNulls(b)
            if len(b) == 0:
                del dct[a]
        elif b == None:
            del dct[a]
    return dct


def preparePathForFile(filePathName):
    destFolder = os.path.dirname(filePathName)
    if not os.path.exists(destFolder):
        os.makedirs(destFolder, 0755)


def deepCopyList(inp):
    for vl in inp:
        if isinstance(vl, list):
            yield list(deepCopyList(vl))
        elif isinstance(vl, dict):
            yield deepCopyDict(vl)
        else:
            yield vl


def deepCopyDict(inp):
    outp = inp.copy()
    for ky, vl in outp.iteritems():
        if isinstance(vl, dict):
            outp[ky] = deepCopyDict(vl)
        elif isinstance(vl, list):
            outp[ky] = list(deepCopyList(vl))
    return outp


def simpleDeepCopy(inp):
    if isinstance(inp, dict):
        return deepCopyDict(inp)
    elif isinstance(inp, list):
        return deepCopyList(inp)
    return inp