# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:58:22 2018

@author: nas7ybruises
"""

x = float(input('Enter a dcimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str(((2**p)*x) - int((2**p)*x)))
    p += 1

num = int((2**p)*x)

result = ''
if num == 0:
    result == '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for _ in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + result)