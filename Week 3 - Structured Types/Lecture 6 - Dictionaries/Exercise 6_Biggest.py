# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:23:07 2018

@author: nas7ybruises
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = []
    for val in aDict.values():
        if len(val) > len(big):
            big = val.copy()
    for key in aDict:
        if aDict[key] == big:
            return key

biggest({'u': [10, 15, 5, 2, 6], 'B': [15]})