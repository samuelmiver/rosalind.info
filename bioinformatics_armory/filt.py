#!/usr/bin/env python

import math
import sys
import os
from Bio import SeqIO

def filt():

    with open('files/rosalind_filt.txt') as fi:
        q, p = map(int, fi.readline().split())
        fastq = fi.read()

    with open('tmp.fastq', 'w') as fo:
        fo.write(fastq)

    number_sequences_filtered = 0
    records = SeqIO.parse('tmp.fastq','fastq')

    for record in records:
        qualities = record.letter_annotations['phred_quality']
        number_bases_above_qthres = sum([1 if b >= q else 0 for b in qualities])

        if number_bases_above_qthres < len(qualities) * p / 100.0:
            number_sequences_filtered += 1

    print number_sequences_filtered

if __name__ == '__main__':
    filt()

    os.system('rm tmp.fastq')
