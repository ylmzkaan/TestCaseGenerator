# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:23:41 2017

@author: kaany
"""

class Node:
    def __init__(self, Id, _type, value, invoke = False, terminate = False):
        self.Id = Id
        self.type = _type
        self.value = value
        self.invoke = invoke
        self.terminate = terminate
        self.child = []
        self.parent = []
        self.childedge = []
        
    def __repr__(self):
        return '{}'.format(self.Id)  
        
    def addChild(self, x):
        self.child.append(x)
        
    def addParent(self, x):
        self.parent.append(x)
        
    def addChildEdge(self, edge):
        self.childedge.append(edge)
    
    def removeChild(self, x):
        self.child.remove(x)
        
    def removeChildEdge(self, x):
        self.childedge.remove(x)
        
        