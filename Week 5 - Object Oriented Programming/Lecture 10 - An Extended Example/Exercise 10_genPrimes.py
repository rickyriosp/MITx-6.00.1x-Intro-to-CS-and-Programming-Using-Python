# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:51:21 2018

@author: nas7ybruises
"""

def genPrimes():
    num = 1
    while True:
        num += 1
        prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num
