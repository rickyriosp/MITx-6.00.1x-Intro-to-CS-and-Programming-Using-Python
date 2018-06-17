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
    global numFibCalls
    numFibCalls += 1
    return 1 if x==0 or x==1 else fib(x-1) + fib(x-2)

def fib_efficient(n, d):
    """
    Assumes x an int >= 0
    Returns Fibonacci of x
    """
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + d[n-2]
        d[n] = ans
        return ans

d = {1:1, 2:2}

num = 34
numFibCalls = 0
print ('Using fib')
print(fib(num))
print('Number of function calls', numFibCalls)

numFibCalls = 0
print()
print('Using fib_efficient')
print(fib_efficient(num, d))
print('Number of function calls', numFibCalls)