# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:10:21 2018

@author: nas7ybruises
"""

def getSublists(L, n):
    '''
    L: list of integers
    n: length of sublists
    '''
    return [L[i:i+n] for i in range(len(L)-n+1)]

print(getSublists([1, 1, 1, 1, 4], 2))