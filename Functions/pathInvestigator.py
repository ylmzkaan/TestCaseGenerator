# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:54:34 2017

@author: kaany
"""

def pathInvestigator(currentNode, mapkey, memory = [[]], path = [[]], i = 0, freshNode = True):
    if currentNode.terminate == True: #if this new node is the final node then do the following
        currentNode = mapkey[memory[-1][-1].target] #return back to the last node in memory
        currentNode.removeChildEdge(currentNode.childedge[0]) #delete the new node's first childedge since we already went through it
        freshNode = False
        
        if len(currentNode.childedge) == 0: #if there is no child left in the memorized node, do the following          
            del memory[-1] #delete the memorized node that has no child
            if memory == [[]]: #if there is no node left in the memory then return the paths found
                return path
            currentNode = mapkey[memory[-1][-1].target] #make the currentNode the last remember node in the edited memory
            currentNode.removeChildEdge(currentNode.childedge[0])
            i += 1 #new path
            path.append(list(memory[-1])) #in the next path continue adding edges starting from the last memory
        
        else: #if there is still child in the node then do the following
            i += 1 #we are starting a new path, so add a new row to the path list
            path.append(list(memory[-1])) #new row of path contains the nodes from the last memory
    else:
        #iterate to next child node
        if len(currentNode.childedge) > 0:
            path[i].append(currentNode.childedge[0])
            currentNode = mapkey[currentNode.childedge[0].target] #make the currentNode preceeding currentNode's child
            freshNode = True
    #if current node has more than one child and if it is not in memory, then add the path until that node to memory
    if len(currentNode.childedge) > 1 and path[i] not in memory and freshNode == True: #if currentNode has more than one child then do the following
        memory.append(tuple(path[i])) #remember the path that leads to this node
        
    return pathInvestigator(currentNode, mapkey, memory, path, i, freshNode)
