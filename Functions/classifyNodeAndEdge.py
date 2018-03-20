# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:01:42 2018

@author: kaany
"""
from Classes.Classes import Node, Edge

#For every mxcell struct, find if there is an ellipse node or an edge that 
#names an edge and saves them all to different lists for postprocessing
#nodes edges and texts have unique Id attributes to be identified. 

def main(xmlRoot):
    nodes = list()
    invokeAndTerminateNodes = list()
    edges = list()
    for _object in xmlRoot.iter('mxCell'):
        try:  
            nodes, edges, invokeAndTerminateNodes = classifyNodeAndEdges(_object, nodes, 
                                                                         edges, invokeAndTerminateNodes)
        except AttributeError:
            pass
    nodes = insertInvokeAndTerminateNodesToOtherNodes(nodes, invokeAndTerminateNodes)
    return nodes, edges

def classifyNodeAndEdges(_object, nodes, edges, invokeAndTerminateNodes):
    
    Id, value, splittedStyle = getObjectProperties(_object)
    nodes, edges, invokeAndTerminateNodes = classifyObject(Id, value, splittedStyle, 
                                                           nodes, edges, _object, 
                                                           invokeAndTerminateNodes)
    return nodes, edges, invokeAndTerminateNodes

def getObjectProperties(_object):
    style = _object.get('style')
    splittedStyle = style.split(';')
    Id = _object.get('id')
    value = _object.get('value')
    return Id, value, splittedStyle

def classifyObject(Id, value, splittedStyle, nodes, edges, _object, invokeAndTerminateNodes):
    if isFunction(splittedStyle): 
        nodes.append(Node(Id, "function", value)) 
    elif isState(splittedStyle):
        #Value 'invoke' refers to the invoking node
        if value.lower() == 'invoke':
            invokeAndTerminateNodes.insert(0, Node(Id, "Invoke", value, True, False)) 
        #Value 'terminate' refers to the terminating node
        elif value.lower() == 'terminate':
            invokeAndTerminateNodes.append(Node(Id, "Terminate", value, False, True))
        #Else, this node is an ordinary state node
        else:
            nodes.append(Node(Id, "state", value)) 
    elif isIf(splittedStyle): 
        nodes.append(Node(Id, "if", value))
    elif isEdge(splittedStyle): 
        targetNode = _object.get('target')
        sourceNode = _object.get('source')
        edges.append(Edge(Id, sourceNode, targetNode))
    return nodes, edges, invokeAndTerminateNodes
        
def isFunction(style):
    if 'ellipse' in style[0]:
        return True
    return False

def isState(style):
    if 'rounded' in style[0] or 'shape=callout' in style[0]:
        return True
    return False

def isIf(style):
    if 'rhombus' in style[0]:
        return True
    return False

def isEdge(style):
    if 'edgeStyle' in style[0]: 
        return True
    return False    

def insertInvokeAndTerminateNodesToOtherNodes(nodes, invokeAndTerminateNodes):
    nodes.append(invokeAndTerminateNodes[-1])
    nodes.insert(0, invokeAndTerminateNodes[0])
    return nodes