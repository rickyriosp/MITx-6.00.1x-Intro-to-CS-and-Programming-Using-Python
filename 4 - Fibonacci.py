# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:18:54 2018

@author: nas7ybruises
"""

def fib(x):
    """
    Assumes x an int >= 0
    Returns Fibonacci of x
    """
    return 1 if x==0 or x==1 else fib(x-1) + fib(x-2)