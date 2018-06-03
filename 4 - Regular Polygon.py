# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:27:49 2018

@author: nas7ybruises
"""
from math import *

def polysum(n, s):
    '''
    Takes two arguments (n, s) -> can be int or float
    
    Returns the sum of the area and square of the perimeter of 
    the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    '''
    ans = (n*s)**2      # Square of perimeter
    ans += (0.25*n*s**2)/tan(pi/n)
    return round(ans, 4)