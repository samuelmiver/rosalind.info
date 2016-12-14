#!/usr/bin/env python

from igraph import *

n = False
g = Graph()
edges = []
with open('files/rosalind_tree.txt', 'r') as fi:
    for line in fi:
        if not n:
            n = int(line.strip())
            g.add_vertices(n+1)
        else:
            edges.append([int(x) for x in line.strip().split()])
g.add_edges(edges)

print len(g.clusters())-2 # -1 because yes, -2 because the tree starts on 0
