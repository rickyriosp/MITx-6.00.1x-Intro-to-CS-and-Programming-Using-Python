# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:26:43 2018

@author: nas7ybruises
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N == 0:
        return 0
    else:
        return sumDigits(N//10) + N % 10

print(sumDigits(56))