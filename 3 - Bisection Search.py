# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:05:48 2018

@author: nas7ybruises
"""

# Square root
x = 0.25
epsilon = 0.01
numGuesses = 0
ans = (low+high)/2.0
if x >= 1:
    low = 0
    high = x
else:
    low = x
    high = 1

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))

# Cube root
cube = 0.729
epsilon = 0.01
numGuesses = 0
ans = (low+high)/2.0
if x >= 1:
    low = 0
    high = x
else:
    low = x
    high = 1

while abs(ans**3 - cube) >= epsilon:
    numGuesses += 1
    if ans**3 < cube:
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the cube root of ' + str(cube))