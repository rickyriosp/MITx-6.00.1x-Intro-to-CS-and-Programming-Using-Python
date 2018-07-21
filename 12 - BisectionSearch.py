# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 16:20:40 2018

@author: nas7ybruises
"""

def bisection_search(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)