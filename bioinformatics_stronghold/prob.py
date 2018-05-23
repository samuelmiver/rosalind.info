#!/usr/bin/env python

import numpy as np

def compute_prob(s, GCcontent):

    probs = {'A':(1-GCcontent)/2, 'T':(1-GCcontent)/2, 'G':GCcontent/2, 'C':GCcontent/2}
    return np.log10(np.prod(np.array([probs[nt] for nt in s])))

def prob(fil):

    s = False
    A = False
    with open(fil, 'rU') as fi:
        for line in fi:
            if s:
                A = [float(i) for i in line.strip().split()]
            else:
                s = line.strip()

    result = []
    for GC in A:
        result.append(compute_prob(s, GC))

    print ' '.join([str(i) for i in result])




if __name__ == '__main__':
    prob('./files/rosalind_prob.txt')
