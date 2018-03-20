# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:08:09 2018

@author: kaany
"""

def writeToTxt(nodeList):
    output = open("Output.txt","w")
    output.write("\t" + "Initial State\t\t Step\t\t Output" + "\n")
    try:
        for i, row in enumerate(nodeList):
            output.write("\n" + "Path" + str(i+1) + "\n")
            for node in row:
                    try:
                        output.write(node.value + "\t")
                    except AttributeError:
                        pass
    finally:
        output.close()