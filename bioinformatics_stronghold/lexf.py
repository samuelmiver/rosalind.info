#!/usr/bin/env python

from itertools import product

def lexf(inFile):

    # Process the file
    with open(inFile) as fi:
        alphabet, n = fi.readlines()
        alphabet    = ''.join(alphabet.split())
        n           = int(n)

    # Generate all the possible subsequences
    print ' '.join(sorted([''.join(i) for i in product(alphabet, repeat = n)]))

if __name__ == '__main__':
    lexf('./files/rosalind_lexf.txt')

