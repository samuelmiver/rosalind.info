#!/usr/bin/env python3

def deg():
    """
    Given a edge list format file, it returns the degree of each edge
    """

    graphito = []
    number_set = set()

    with open('./files/rosalind_deg.txt', 'r') as f:
        next(f)
        count = 0
        for line in f:
            line = line.strip().split()
            edgeA = int(line[0])
            edgeB = int(line[1])

            number_set.add(edgeA)
            number_set.add(edgeB)

            graphito.append(edgeA)
            graphito.append(edgeB)

    results = []
    for element in number_set:
        degree = graphito.count(element)

        results.append(degree)

    result = [str(x) for x in results]
    print(' '.join(result))


if __name__ == '__main__':
    deg()
