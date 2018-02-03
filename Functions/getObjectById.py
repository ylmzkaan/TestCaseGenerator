# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 01:03:17 2018

@author: kaany
"""

def getObjectById(string, objectlist):
    for i in objectlist:
        if str(string) == str(i):
            return i
    return False