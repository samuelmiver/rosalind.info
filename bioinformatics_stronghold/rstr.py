#!/usr/bin/env python

import numpy as np

def rstr(inFile):
    with open(inFile, 'r') as fi:
        for line in fi:
            line = line.split()
            if len(line)==2:
                N = int(line[0])
                x = float(line[1])
            else:
                s = str(line[0])

    # Probability of the seq
    p = np.prod([x/2.0 if nt in ['G', 'C'] else (1.0-x)/2.0 for nt in s])

    return round(1-(1-p)**N, 3)

if __name__=='__main__':
    print rstr('./files/rosalind_rstr.txt')
