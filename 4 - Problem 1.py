# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:57:20 2018

@author: nas7ybruises
"""

# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the 
# credit card company each month.
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for _ in range(12):
    balance -= balance * monthlyPaymentRate
    balance += balance * (annualInterestRate/12)
print(round(balance, 2))