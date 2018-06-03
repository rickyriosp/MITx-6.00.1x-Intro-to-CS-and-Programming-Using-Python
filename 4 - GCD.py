# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:42:24 2018

@author: nas7ybruises
"""

# Iterative
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for i in range(min(a, b), 1, -1):
        if a%i==0 and b%i==0:
            return i
    return 1


# Recursive
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    return a if b==0 else gcdRecur(b, a % b)