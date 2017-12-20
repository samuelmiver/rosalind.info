#!/usr/bin/env python

import math
import sys
import os

def filt():

    with open('files/rosalind_filt.txt') as fi:
        q, p = map(str, fi.readline().split())
        fastq = fi.read()

    with open('files/tmp.fastq', 'w') as fo:
        fo.write(fastq)

    # Run fastq quality filter
    cmd = 'fastq_quality_filter -q '+q+' -p '+p+' -Q33 -i files/tmp.fastq -o files/filtered.fastq'
    os.system(cmd)

    num_lines = sum(1 for line in open('files/filtered.fastq'))
    print num_lines/4

if __name__ == '__main__':
    filt()

    os.system('rm files/tmp.fastq files/filtered.fastq')
