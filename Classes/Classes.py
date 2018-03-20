# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:23:41 2017

@author: kaany
"""

class Node:
    def __init__(self, Id, _type, value, invoke=False, terminate=False):
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
        
    def addChild(self, childNode):
        self.child.append(childNode)
        
    def addParent(self, parentNode):
        self.parent.append(parentNode)
        
    def addChildEdge(self, childEdge):
        self.childedge.append(childEdge)
    
    def removeChild(self, childNode):
        self.child.remove(childNode)
        
    def removeChildEdge(self, childEdge):
        self.childedge.remove(childEdge)
        
class Edge:
    def __init__(self, Id, sourceNode, targetNode, sourceNodeValue=0, targetNodeValue=0):
        self.Id = Id
        self.sourceNode = sourceNode
        self.targetNode = targetNode
        self.sourceNodeValue = sourceNodeValue
        self.targetNodeValue = targetNodeValue
    
    def __repr__(self):
        return '{}'.format(self.Id)  
                
    def addSourceNodeValue(self, sourceNodeValue):
        self.sourceNodeValue = sourceNodeValue
        
    def addTargetNodeValue(self, targetNodeValue):
        self.targetNodeValue = targetNodeValue
        
        