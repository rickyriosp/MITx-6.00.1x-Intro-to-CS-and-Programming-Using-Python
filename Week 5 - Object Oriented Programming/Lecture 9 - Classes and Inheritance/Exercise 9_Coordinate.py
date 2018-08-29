# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:09:07 2018

@author: nas7ybruises
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        return 'Coordinate(%d,%d)' % (self.x, self.y)
