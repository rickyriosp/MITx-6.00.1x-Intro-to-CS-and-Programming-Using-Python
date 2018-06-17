# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:25:44 2018

@author: nas7ybruises
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    size = []
    for val in aDict.values():
        size.append(val)
    return len(size)

how_many({'u': [10, 15, 5, 2, 6], 'B': [15]})
