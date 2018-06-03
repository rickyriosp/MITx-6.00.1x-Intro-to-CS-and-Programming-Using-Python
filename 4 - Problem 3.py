# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:35:35 2018

@author: nas7ybruises
"""

balance = 999999
annualInterestRate = 0.18
epsilon = 0.05
low = balance/12
high = (balance * (1 + annualInterestRate/12))**12 / 12
remainder = balance

while abs(remainder) >= epsilon:
    remainder = balance
    monthlyPayment = (low + high)/2
    for _ in range(12):
        remainder -= monthlyPayment
        remainder += remainder * (annualInterestRate/12)
    if remainder > 0:
        low = monthlyPayment
    else:
        high = monthlyPayment
        
print(round(monthlyPayment, 2))