# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:16:53 2018

@author: nas7ybruises
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = []
    for key in aDict.keys():
        if aDict[key] == target:
            keys.append(key)
    return sorted(keys)
