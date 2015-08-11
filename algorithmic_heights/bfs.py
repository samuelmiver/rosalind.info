#!/usr/bin/env python

from collections import defaultdict


def minimum_path_bfs(n, edges):

    # Build the graph.
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)

    # BFS to find the minimum distance to each node from node 1.
    min_dist = [0] + [-1]*(n-1)
    remaining = set(xrange(2, n+1))
    queue = [1]
    while queue:
        current = queue.pop(0)
        for node in graph[current]:
            if node in remaining:
                queue.append(node)
                remaining.discard(node)
                # Rosalind starts indices at 1 instead of 0.
                min_dist[node-1] = min_dist[current-1] + 1

    return min_dist


def main():
    # Read the input data.
    with open('files/rosalind_bfs.txt') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

    # Get the minimum distances.
    min_dist = map(str, minimum_path_bfs(n, edges))

    # Print and save the answer.
    print ' '.join(min_dist)

if __name__ == '__main__':
    main()
