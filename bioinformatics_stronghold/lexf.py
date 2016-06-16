#!/usr/bin/env python

from itertools import product
from string import ascii_lowercase

def lexf(inFile):

    # Process the file
    l = []
    alphabet = None
    with open(inFile, 'r') as fi:
        for line in fi:
            line = line.strip()
            if not alphabet:
                alphabet = line.replace(' ','')
            else:
                n = int(line)

    # Generate all the possible subsequences
    print '\n'.join([''.join(i) for i in product(alphabet, repeat = n)])

if __name__ == '__main__':
    lexf('./files/rosalind_lexf.txt')

