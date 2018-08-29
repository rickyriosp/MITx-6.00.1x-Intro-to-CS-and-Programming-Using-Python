# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 09:30:46 2018

@author: nas7ybruises
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return sum([0 if i in lettersGuessed else 1 for i in secretWord]) == 0
