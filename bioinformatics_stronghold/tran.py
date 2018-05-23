#!/usr/bin/env python

import numpy as np
import utils as u


def tran(fil):

    seqs = u.load_multifasta(fil)
    seqA, seqB = seqs.values()

    transvrs = 0.0
    transits = 0.0

    for n, m in zip(seqA, seqB):
        if n!=m:
            l = [n, m]
            if sorted(l) in [['A', 'G'], ['C', 'T']]:
                transits+=1
            else:
                transvrs+=1

    print transits/transvrs


if __name__ == '__main__':
    tran('./files/rosalind_tran.txt')
