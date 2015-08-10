#!/usr/bin/env python3

def ddeg():
    """
    Given a edge list format file, it returns the degree of each edge
    """

    graphito = []
    number_set = set()

    with open('./files/rosalind_ddeg.txt', 'r') as f:
        for line in f:
            line = line.strip().split()
            edge_number = int(line[0])
            break

    with open('./files/rosalind_ddeg.txt', 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split()
            edgeA = int(line[0])
            edgeB = int(line[1])

            number_set.add(edgeA)
            number_set.add(edgeB)

            graphito.append(edgeA)
            graphito.append(edgeB)

    results = {}
    for element in number_set:
        degree = graphito.count(element)
        results[element] = degree

    final = {}
    with open('./files/rosalind_ddeg.txt', 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split()
            edgeA = int(line[0])
            edgeB = int(line[1])

            if edgeA in final:
                pass
            else:
                final[edgeA] = []
            if edgeB in final:
                pass
            else:
                final[edgeB] = []

            final[edgeA].append(results[edgeB])
            final[edgeB].append(results[edgeA])


    final_results = []
    for k, v in final.items():
        v = sum(v)
        final_results.append(v)

    # ADD 0 VALUES
    numberofzeros = edge_number - len(final_results)

    while numberofzeros > 0:
        final_results.append(0)
        numberofzeros -= 1


    to_print = [str(x) for x in final_results]
    print(' '.join(to_print))


if __name__ == '__main__':
    ddeg()
