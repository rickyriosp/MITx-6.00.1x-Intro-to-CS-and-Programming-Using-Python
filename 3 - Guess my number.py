# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:05:48 2018

@author: nas7ybruises
"""

low = 0
high = 100
ans = (low+high)//2
user = ''

print('Please think of a number between 0 and 100!')
while user != 'c':
    print('Is your secret number', str(ans) + '?')
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to " \
             "indicate the guess is too low. Enter 'c' to indicate I guessed " \
             "correctly. ")
    while user not in ['l', 'h', 'c']:
        print('Sorry, I did not understand your input.')
        print('Is your secret number', str(ans) + '?')
        user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to " \
             "indicate the guess is too low. Enter 'c' to indicate I guessed " \
             "correctly. ")
        
    if user == 'l':
        low = ans
    elif user == 'h':
        high = ans
    ans = (low+high)//2
    
print('Game over. Your secret number was:', ans)