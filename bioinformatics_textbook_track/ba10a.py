#!/usr/bin/env python

import sys
import os


def process_file(filename):
    """
    Processes the file given to extract the required information
    """

    with open(filename, 'r') as fi:
        fromA = {}
        fromB = {}

        c = 1
        for line in fi:
            if c == 1:
                sequence = str(line.strip())
            elif c == 6:
                line = line.strip().split()
                fromA["A"] = float(line[1])
                fromA["B"] = float(line[2])
            elif c == 7:
                line = line.strip().split()
                fromB["A"] = float(line[1])
                fromB["B"] = float(line[2])
            else:
                pass

            c += 1
    return [sequence, fromA, fromB]


def main(inFile):
    """
    Runs the main function
    """

    x = process_file(inFile)

    sequence = x[0]

    fromA = x[1]
    fromB = x[2]

    n = 0
    score = 1

    while n < len(sequence):
        current_nt = sequence[n]
        next_nt = sequence[n]

        else:
            score *= fromA[next_nt]
        n += 1
            score *= fromB[next_nt]
    print score

if __name__ == '__main__':

    main(sys.argv[1])
