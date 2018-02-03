# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:46:11 2017

@author: kaany
"""

import xml.etree.ElementTree as ET
from Classes.edge import Edge
from Classes.node import Node

from Functions.attrFinder import AttrFinder
from Functions.pathInvestigator import pathInvestigator
from Functions.extractnodefrompath import ExtractNodefromPath

#xml file to be imported
file = "deneme2.xml" 

#get to the root of the xml file
tree = ET.parse(file)
root = tree.getroot()

#lists in which the nodes edges etc. will be stored in for postprocessing
startend = list()
nodes = list()
edges = list()
loopingEdges = list()
texts = list()
paths = list()
mapkey = dict()

# for every mxcell struct, find if there is an ellipse node or an edge or a text that names an edge and saves them all to different lists for postprocessing
#nodes edges and texts have unique Id attributes to be identified. Id attr is read from the xml
for x in root.iter('mxCell'):
    try:
        style = x.get('style')
        style_split = style.split(';')
        Id = x.get('id')
        value = x.get('value')
        if 'ellipse' in style_split[0]: # ellips is function or button
            nodes.append(Node(Id, "function", value)) #create a Node object and save it to nodes list
        
        elif 'rounded' in style_split[0]:  # rounded(rectangle) is state
            if value.lower() == 'invoke':
                startend.insert(0, Node(Id, "Invoke", value, True, False)) 
            elif value.lower() == 'terminate':
                startend.append(Node(Id, "Terminate", value, False, True))
            else:
                nodes.append(Node(Id, "state", value)) 
        
        elif 'shape=callout' in style_split[0]: #state
            nodes.append(Node(Id, "state", value))
        
        elif 'rhombus' in style_split[0]: #if
            nodes.append(Node(Id, "If", value))
        
        elif 'edgeStyle' in style_split[0]: #if the first element of style_split is edgeStyle then this mxcell is an edge
            target = x.get('target')
            source = x.get('source')
            edges.append(Edge(Id, source, target))
    except AttributeError:
        pass

nodes.append(startend[-1])
nodes.insert(0, startend[0])


    
#map source and target of an edge to corresponding nodes using their Ids
for y in edges:
    if y.source not in list(mapkey.keys()): #add source node to mapkey
        mapkey[y.source] = AttrFinder(nodes, 'Id', y.source)  
    if y.target not in list(mapkey.keys()): #add target node to mapkey
        mapkey[y.target] = AttrFinder(nodes, 'Id', y.target)
    if y.Id not in list(mapkey.keys()): # add edge to mapkey
        mapkey[y.Id] = y
    if y.source == y.target: # if any looping edge then add it to loopingEdges list and remove it from edges
        loopingEdges.append(y)
        edges.remove(y)
        
for y in edges: #for every edge add child childedge and parent to nodes
    try: 
        mapkey[y.source].addChild(mapkey[y.target])
        mapkey[y.source].addChildEdge(y)
        mapkey[y.target].addParent(mapkey[y.source])
        y.addSourceValue(mapkey[y.source].value) #add the value of source node to edge
        y.addTargetValue(mapkey[y.target].value)
    except AttributeError:
        pass

paths = pathInvestigator(nodes[0], mapkey) #Extract the paths
for y in loopingEdges: #Add looping edges to paths
    for row in paths:
        i = 0
        for edge in row:
            if edge.target.Id == y.source:
                row.insert(i+1, y)
            i += 1
            
Nodepaths = ExtractNodefromPath(paths, mapkey)

output = open("Output.txt","w")
output.write("\t" + "Initial State\t\t Step\t\t Output" + "\n")
i = 1
for row in Nodepaths:
    output.write("\n" + "Path" + str(i) + "\n")
    i += 1
    for node in row:
            try:
                output.write(node.value + "\t")
            except AttributeError:
                pass
output.close()

        