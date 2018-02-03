# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:38:46 2017

@author: kaany
"""

class Edge:
    def __init__(self, Id, source, target, s_value = 0, t_value = 0):
        self.Id = Id
        self.source = source
        self.target = target
        self.s_value = s_value
        self.t_value = t_value
    
    def __repr__(self):
        return '{}'.format(self.Id)  
        
    def addText(self, text):
        self.text = text
        
    def addSourceValue(self, x):
        self.s_value = x
        
    def addTargetValue(self, x):
        self.t_value = x