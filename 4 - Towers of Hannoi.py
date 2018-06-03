# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:08:42 2018

@author: nas7ybruises
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(3, 'P1', 'P2', 'Spare'))