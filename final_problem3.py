# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:28:03 2018

@author: nas7ybruises
"""

#def isPalindrome(aString):
#    '''
#    aString: a string
#    Returns True if aString is palindrome, False otherwise
#    '''
#    if len(aString) < 2:
#        return True
#    elif len(aString) == 2:
#        return aString[0] == aString[1]
#    else:
#        return isPalindrome(aString[1:-1])


def isPalindrome(aString):
    '''
    aString: a string
    Returns True if aString is palindrome, False otherwise
    '''
    left = 0
    right = len(aString)-1    
    for i in range(len(aString)//2):
        if aString[left] != aString[right]:
            return False
        left += 1
        right -= 1
    return True
