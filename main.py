# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:46:11 2017

@author: kaany
"""

import xml.etree.ElementTree as ET
from Functions.mapIdToObjects import mainGetIdToObjectMap, addLoopingEdgesToPaths
from Functions.path import pathCalculator
from Functions import classifyNodeAndEdge
from Functions.report import writeToTxt

"""
In order to do a Model Based Testing, a tester has to know most of the every possible combination 
of inputs that may be given by an end-user. Seeing all the possible inputs using a flowchart is 
hard.

This function, extracts every possible path from a flowchart that contains states and functions 
that can be encountered while using the product. This flowchart should be arranged on draw.io . 

The flowchart should have nodes which represent either as state or function. Nodes should be 
connected with edges.

There has to be one invoke node. All paths should start from invoke node. Invoke node has to be
rectangle and its value should be 'invoke'.
 
There has to be a terminate node. All paths should end in this node. Terminate node has to be
rectangle and its value should 'terminate'.

A program has functions and states. Functions may be buttons, sliders etc. States and functions are
the main elements of a flowchart.

"Function" in a flowchart appears to be nodes. However, these nodes has to be rectangle on draw.io
and its value has to be other than 'invoke' or 'terminate' in order for this program to understand 
the nodes as functions.

"State" in a flowchart appears to be nodes. These nodes has to be ellipse on draw.io
in order for this program to understand the nodes as states.

Every node has at least one child, parent or childedge. Nodes are connected to each other by edges.

In order to use this program create your flowchart on draw.io and extract it as XML to your computer
and BE SURE TO UNCHECK 'Compressed' BEFORE EXPORTING.

This script:
    Takes a flowchart as XML format as input.
    Then;
    1- Parses the root of XML file(flowchart) which is created on draw.io 
    2- Exracts all nodes and edges drawn on the flowchart
    3- Creates a dictionary that acts as a map which allows accessing edge and node objects
        by their Ids
    4- Extracts all possible paths from the flowchart excluding the looping edges
    (An edge whose source node and target node are the same is called a looping edge.)
    5- Includes the looping edges to the corresponding paths
    6- Reports all paths by writing every nodes' value(text written on the node) on a path 
    to a .txt file
"""

def main(file):
    """ PARSE XML FILE """
    #Get the root of the XML file
    tree = ET.parse(file)
    XMLroot = tree.getroot()
    
    """ EXTRACT NODES AND EDGES FROM XML """
    #Parse XML to obtain edge and node objects
    nodes, edges = classifyNodeAndEdge.main(XMLroot)
        
    """ MAP OBJECT IDs TO ITS OBJECT """
    #Map object Ids to objects. Add childs, parents and childedges to nodes
    idToObject, loopingEdges = mainGetIdToObjectMap(nodes, edges)
    
    """ EXTRACT ALL POSSIBLE PATHS """
    #Extract all possible paths from nodes
    pc = pathCalculator(nodes, idToObject)
    paths = pc.main(nodes[0]) 
    
    #Insert looping edges to corresponding paths
    paths = addLoopingEdgesToPaths(loopingEdges, paths)
    
    """ REPORT TO A TXT FILE """
    #Get each path's nodes for easy writing to file
    nodeList = pc.extractNodefromPaths()
    
    #Report each path's nodes to .txt 
    writeToTxt(nodeList)

""" GET DATA """
#Define XML file
file = "deneme2.xml" 

if __name__ == "__main__":
    main(file)