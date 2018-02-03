# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:54:34 2017

@author: kaany
"""

def pathInvestigator(currentNode, mapkey, memory = [[]], path = [[]], i = 0):
    print(currentNode.value)
    if currentNode.terminate == True: #if this new node is the final node then do the following 
        currentNode = mapkey[memory[-1][-1].target] #return back to the last memory node
        currentNode.removeChild(mapkey[currentNode.childedge[0].target]) #delete this new node's first child because we already went through it
        currentNode.removeChildEdge(currentNode.childedge[0]) #delete the new node's first childedge since we already went through it
        freshNode = True #this means that the current node is already in memory
        
        if len(currentNode.child) == 0: #if there is no child left in the memorized node do the following          
            del memory[-1] #delete the memorized node that has no child
            if memory == [[]]: #if there is no node in the memory then return the paths found
                return path
            currentNode = mapkey[memory[-1][-1].target] #make the currentNode the last remember node in the edited memory
            currentNode.removeChild(mapkey[currentNode.childedge[0].target]) #delete this new node's first child because we already went through it
            currentNode.removeChildEdge(currentNode.childedge[0]) #delete the new node's first childedge since we already went through it
            i += 1
            path.append(list(memory[-1])) #update the path because we'll iterate over a different node in the memory
        
        else: #if there is still child in the node do the following
            i += 1 #we are starting a new path, so add a new row to the path list
            path.append(list(memory[-1])) #new row of path contains the nodes from our memory, we'll iterate along the memory
    else:
        if currentNode.childedge[0] not in path[i]:
            path[i].append(currentNode.childedge[0])
            currentNode = mapkey[currentNode.childedge[0].target] #make the currentNode preceeding currentNode's child
            freshNode = False #it means current node isnt in memory
        else:
            currentNode.removeChild(mapkey[currentNode.childedge[0].target]) #delete this new node's first child because we already went through it
            currentNode.removeChildEdge(currentNode.childedge[0]) #delete the new node's first childedge since we already went through it
            if len(currentNode.childedge) > 0:
                path[i].append(currentNode.childedge[0])
                currentNode = mapkey[currentNode.childedge[0].target] #make the currentNode preceeding currentNode's child
                freshNode = False
            else:
                currentNode.terminate = True
                
    if len(currentNode.child) > 1 and path[i] not in memory and freshNode == False: #if currentNode has more than one child then do the following
        memory.append(tuple(path[i])) #remember the path that leads to this node
    return pathInvestigator(currentNode, mapkey, memory, path, i)