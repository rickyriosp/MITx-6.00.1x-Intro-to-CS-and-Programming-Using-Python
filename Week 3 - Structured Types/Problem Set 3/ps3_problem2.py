# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:40:00 2018

@author: nas7ybruises
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([c if c in lettersGuessed else '_' for c in secretWord])
