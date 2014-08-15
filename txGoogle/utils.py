'''
Created on 15 aug. 2014

@author: sjuul
'''


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
