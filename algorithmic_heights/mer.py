#!/usr/bin/env python

def mer():
    with open('./files/rosalind_mer.txt', 'r') as f:
        lines = []
        for line in f:
            line = line.strip().split()
            new_line = line

            lines += [new_line,]

    # Process the content
    n = int(lines[0][0])
    m = int(lines[2][0])

    arrayA = [int(x) for x in lines[1]]
    arrayB = [int(x) for x in lines[3]]

    arrayA += arrayB
    arrayA.sort()

    print(' '.join([str(x) for x in arrayA]))

if __name__ == "__main__":
    mer()
