# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:49:34 2018

@author: nas7ybruises
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([c for c in string.ascii_lowercase if c not in lettersGuessed])
