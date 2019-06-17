#!/usr/bin/env python

import utils as u
import sys
sys.path.append('../bioinformatics_stronghold')
from hamm import SNP_counter


seqs = u.load_multifasta('./files/rosalind_subo.txt').values()

def hamm_counter(seqs, dist=3):
    """Count number of matches within dist mismatches."""
    seqA, seqB = seqs
    count = 0
    lA, lB = len(seqA), len(seqB)
    for i in range(lB - lA + 1):
        print i
        if SNP_counter([seqB[i:i + lA], seqA]) <= dist:
            count += 1
    return count

print hamm_counter(seqs), hamm_counter(seqs[::-1])




