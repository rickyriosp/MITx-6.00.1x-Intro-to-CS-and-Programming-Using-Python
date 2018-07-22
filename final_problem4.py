# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:39:02 2018

@author: nas7ybruises
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc_max = 0
    inc_start = 0
    dec_max = 0
    dec_start = 0
    
    def find_inc():
        max_i = 1
        idx = 0
        start, size = 0, 0
        for i in range(1, len(L)):
            if L[i] >= L[i-1]:
                max_i += 1
            else:
                if max_i > size:
                    size = max_i
                    start = idx
                max_i = 1
                idx = i
        if max_i > size:
            size = max_i
            start = idx
        return start,size
            
    def find_dec():
        max_i = 1
        idx = 0
        start, size = 0, 0
        for i in range(1, len(L)):
            if L[i] <= L[i-1]:
                max_i += 1
            else:
                if max_i > size:
                    size = max_i
                    start = idx
                max_i = 1
                idx = i
        if max_i > size:
            size = max_i
            start = idx
        return start,size
    
    inc_start, inc_max = find_inc()
    #print('inc_start:', inc_start, 'inc_max:', inc_max)
    dec_start, dec_max = find_dec()
    #print('dec_start:', dec_start, 'dec_max:', dec_max)
    if inc_max > dec_max:
        return sum(L[inc_start:inc_start+inc_max])
    elif dec_max > inc_max:
        return sum(L[dec_start:dec_start+dec_max])
    elif inc_start < dec_start:
        return sum(L[inc_start:inc_start+inc_max])
    else:
        return sum(L[dec_start:dec_start+dec_max])










