# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 01:17:24 2017

@author: kaany
"""

def AttrFinder(array, attr, key):
    for x in array:
        if getattr(x, attr) == key:
            return x
    return False
        
    