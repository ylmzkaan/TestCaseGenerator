# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:43:32 2018

@author: kaany
"""

def ExtractNodefromPath(path, mapkey):
    nodepath = list()
    i = 0
    for row in path:
        nodepath.append(list())
        for edge in row:
            nodepath[i].append(mapkey[edge.target])
        i += 1
    return nodepath
