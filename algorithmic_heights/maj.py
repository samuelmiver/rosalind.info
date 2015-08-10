#!/usr/bin/env python

def maj():
    with open('./files/rosalind_maj.txt', 'r') as f:
        lines = []
        for line in f:
            line = line.strip().split()
            new_line = line

            lines += [new_line,]

    # Process the content
    k = int(lines[0][0])
    n = int(lines[0][1])

    arrays = lines[1:]

    final = []
    for array in arrays:
        most_common_element = max(set(array), key=array.count)
        counts = array.count(most_common_element)

        if counts > len(array)//2:
            final.append(most_common_element)
        else:
            final.append(-1)

    print(' '.join([str(x) for x in final]))

if __name__ == "__main__":
    maj()
