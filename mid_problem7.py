# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:32:28 2018

@author: nas7ybruises
"""


def f(n, x):
    return n + x

def score(word, f):
    """
       word: a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f: a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
       score for 'adD' is 12 
    """
    max = [0, 0]
    word = word.lower()
    for i in range(len(word)):
        score = (ord(word[i])-96) * i
        if score > max[1]:
            max[0] = max[1]
            max[1] = score
        elif score > max[0]:
            max[0] = score
    return f(max[1], max[0])   

print(score('adD', f))