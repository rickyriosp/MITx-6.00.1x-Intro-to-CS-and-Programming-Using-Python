# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:43:58 2018

@author: nas7ybruises
"""

num = int(input('Enter a decimal integer number: '))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''
if num == 0:
    result == '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

if isNeg:
    result = '-' + result
    
print('The binary representation is ' + result)