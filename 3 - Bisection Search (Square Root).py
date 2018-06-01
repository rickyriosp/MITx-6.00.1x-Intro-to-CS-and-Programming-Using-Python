# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:05:48 2018

@author: nas7ybruises
"""

x = 49
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (low+high)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))