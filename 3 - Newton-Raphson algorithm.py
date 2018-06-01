# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:26:40 2018

@author: nas7ybruises
"""

# Newton-Raphson aglorithm
# g = g - (g^n-p(g)/p')
y = 54
epsilon = 0.01
guess = y/2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess = guess - (guess**2 - y)/(2*guess)

print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))