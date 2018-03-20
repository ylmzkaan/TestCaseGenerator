# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 01:17:24 2017

@author: kaany
"""

def mainGetIdToObjectMap(nodes, edges):
    #Map Ids of source and target of all edges to their corresponding nodes using node's Ids
    idToObject, loopingEdges = getMapIdToObjects(nodes, edges)
    #Each node has either a child, parent or childege. This function finds them and assigns them
    #to the correct node
    idToObject = addChildParentAndChildEdgeToNodes(edges, idToObject)
    
    return idToObject, loopingEdges

def getMapIdToObjects(nodes, edges):
    """
    Each edge and node object has a unique id. In order to call any edge or node object using
    its id, each id is mapped to its object using a dictionary. Dictionary key is the id and key's
    value is the object itself
    """
    idToObject = dict()
    loopingEdges = list()
    for edge in edges:
        #Add source node of edge to mapKeysToObjects
        idToObject[edge.sourceNode] = getObjectWithSpecificValueOfAttributeFromArray(nodes, 'Id', edge.sourceNode)          
        idToObject[edge.targetNode] = getObjectWithSpecificValueOfAttributeFromArray(nodes, 'Id', edge.targetNode)          
        idToObject[edge.Id] = edge
        #If the edge is looping then add it to loopingEdges list and remove it from edges
        #Looping edges will be dealt later
        if isLoopingEdge(edge): 
            loopingEdges.append(edge)
            edges.remove(edge)
    return idToObject, loopingEdges

def isLoopingEdge(edge):
    if edge.sourceNode == edge.targetNode:
        return True
    return False

def getObjectWithSpecificValueOfAttributeFromArray(array, attr, value):
    for item in array:
        if getattr(item, attr) == value:
            return item
    return False

def addChildParentAndChildEdgeToNodes(edges, idToObject):
    """
    Iterate through edges and for each edge, get its source and target node. Make the target node
    a child of the source node. Also, make the source node a parent of the target node. 
    Add the edge as the childedge of the edge's source node.
    Finally, since when this function is called all the nodes are saved in the idToObject dictionary,
    add the value of the source node's to edge and do the same thing for the target node of the edge.
    """
    for edge in edges:
        try: 
            idToObject[edge.sourceNode].addChild(idToObject[edge.targetNode])
            idToObject[edge.sourceNode].addChildEdge(edge)
            idToObject[edge.targetNode].addParent(idToObject[edge.sourceNode])
            edge.addSourceValue(idToObject[edge.sourceNode].value) 
            edge.addTargetValue(idToObject[edge.targetNode].value)
        except AttributeError:
            pass
    return idToObject

def addLoopingEdgesToPaths(loopingEdges, paths):
    #Add looping edges to paths
    for y in loopingEdges: 
        for row in paths:
            i = 0
            for edge in row:
                if edge.targetNode.Id == y.sourceNode:
                    row.insert(i+1, y)
                i += 1
    return paths