#!/usr/bin/env python

import networkx as nx

def cc():
    with open("./files/rosalind_cc.txt") as f:
        n, m = map(int, f.readline().strip().split())
        lines = f.readlines()

    edge_list = map(lambda x: map(int, x.strip().split()), lines)

    # Create the graph
    nxgraph = nx.Graph()
    nxgraph.add_nodes_from(range(1,n+1))
    nxgraph.add_edges_from(edge_list)

    print len(list(nx.connected_components(nxgraph)))

if __name__ == "__main__":
    cc()
