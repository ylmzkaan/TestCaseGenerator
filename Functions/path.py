# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:54:34 2017

@author: kaany
"""


class pathCalculator:
    def __init__(self, nodes, idToObject, memory=[[]], paths=[[]], pathIndex=0):
        self.nodes = nodes
        self.idToObject = idToObject
        self.memory = memory
        self.paths = paths
        self.pathIndex = pathIndex
        
    def main(self, currentNode):
        paths = pathCalculator.extractPathFromNodes(self, currentNode, freshNode = True)
        return paths
        
    def extractPathFromNodes(self, currentNode, freshNode = True):
        if pathCalculator.isTerminatingNode(currentNode): #if this new node is the final node then do the following
            currentNode = pathCalculator.goToLastMemorysLastNode(self)
            freshNode = False
            if pathCalculator.hasNoChild(currentNode): #if there is no child left in the memorized node, do the following          
                pathCalculator.deleteLastPathInMemory(self)
                if self.memory == [[]]: #if there is no node left in the memory then return the paths found
                    return self.paths
                currentNode = pathCalculator.goToLastMemorysLastNode(self)
                pathCalculator.newPathFormLastMemory(self)
            else: #if there is still child in the node then do the following
                pathCalculator.newPathFormLastMemory(self)
        else:
            #Go to next child node
            if not pathCalculator.hasNoChild(currentNode):
                currentNode = pathCalculator.getChildAndAddItToPath(self, currentNode)
                freshNode = True
        #if current node has more than one child and if it is not in memory, then add the path until that node to memory
        if pathCalculator.hasMultipleChildren(currentNode) and self.paths[self.pathIndex] not in self.memory and freshNode == True: #if currentNode has more than one child then do the following
            self.memory.append(tuple(self.paths[self.pathIndex])) #remember the path that leads to this node
        return pathCalculator.extractPathFromNodes(self, currentNode, freshNode)
    
    def isTerminatingNode(Node):
        if Node.terminate == True:
            return True
        return False
    
    def hasMultipleChildren(Node):
        if len(Node.childedge) > 1:
            return True
        return False
    
    def getChildAndAddItToPath(self, Node):
        self.paths[self.pathIndex].append(Node.childedge[0])
        childNode = self.idToObject[Node.childedge[0].targetNode] #make the currentNode preceeding currentNode's child
        return childNode
    
    def deleteLastPathInMemory(self):
        del self.memory[-1] #delete the memorized node that has no child
        
    def goToLastMemorysLastNode(self):
        currentNode = self.idToObject[self.memory[-1][-1].targetNode] #return back to the last node in memory
        currentNode.removeChildEdge(currentNode.childedge[0]) #delete the new node's first childedge since we already went through it
        return currentNode
    
    def newPathFormLastMemory(self):
        self.pathIndex += 1 #new path
        self.paths.append(list(self.memory[-1])) #in the next path continue adding edges starting from the last memory
        return self.paths, self.pathIndex
    
    def hasNoChild(Node):
        if len(Node.childedge) == 0:
            return True
        return False
    
    def extractNodefromPaths(self):
        nodeList = list()
        for i, path in enumerate(self.paths):
            nodeList.append(list())
            for edge in path:
                nodeList[i].append(self.idToObject[edge.targetNode])
        return nodeList