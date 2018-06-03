# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:08:05 2018

@author: nas7ybruises
"""

# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months. By a
# fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each month.
balance = 42
annualInterestRate = 0.2

monthlyPayment = 0
remainder = balance
while remainder > 0:
    remainder = balance
    monthlyPayment += 10
    for _ in range(12):
        remainder -= monthlyPayment
        remainder += remainder * (annualInterestRate/12)
print(monthlyPayment)