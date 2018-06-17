# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:30:46 2018

@author: nas7ybruises
"""

def fib(x):
    """
    Assumes x an int >= 0
    Returns Fibonacci of x
    """
    return 1 if x==0 or x==1 else fib(x-1) + fib(x-2)

def fib_efficient(n, d):
    """
    Assumes x an int >= 0
    Returns Fibonacci of x
    """
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}

num = 34
print ('Using fib')
print(fib(num))
print()
print('Using fib_efficient')
print(fib_efficient(num, d))