'''
Created on 15 aug. 2014

@author: sjuul
'''
import os
from twisted.python import log
from os import walk
from os.path import getsize


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
    output = []
    for vl in inp:
        if isinstance(vl, list):
            output.append(deepCopyList(vl))
        elif isinstance(vl, dict):
            output.append(deepCopyDict(vl))
        else:
            output.append(vl)
    return output


def deepCopyDict(inp):
    outp = inp.copy()
    for ky, vl in outp.iteritems():
        if isinstance(vl, dict):
            outp[ky] = deepCopyDict(vl)
        elif isinstance(vl, list):
            outp[ky] = deepCopyList(vl)
    return outp


def simpleDeepCopy(inp):
    if isinstance(inp, dict):
        return deepCopyDict(inp)
    elif isinstance(inp, list):
        return deepCopyList(inp)
    return inp


def chunks(lst, maxItems):
    ''' Yield successive n-sized chunks from l.
    '''
    for i in xrange(0, len(lst), maxItems):
        yield lst[i:i + maxItems]


def getFilesInFolder(folderPath, topdown=True, minFileSize=None, stripExtension=None):
    if stripExtension:
        extLen = len(stripExtension)
    for root, _, files in walk(folderPath, topdown=topdown):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            if minFileSize is not None:
                sz = getsize(filePath)
                if sz < minFileSize:
                    try:
                        os.remove(filePath)
                    except:
                        pass
                    continue
            joined = os.path.relpath(filePath, folderPath)
            if stripExtension and joined.endswith(stripExtension):
                joined = joined[:-extLen]
            yield joined
