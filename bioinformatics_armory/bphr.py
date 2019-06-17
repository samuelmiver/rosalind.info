#!/usr/bin/env python

from Bio import SeqIO
import statistics as stat
import sys
import os
import numpy as np

def qphredthreshold(threshold,handle):
    """
    Given a threshold and a FastQ file, prints the number of position with mean quality below the threshold value
    """
    records   = np.array([record.letter_annotations["phred_quality"] for record in handle])
    cons_mean = np.mean(records, axis=0)
    return len(cons_mean[cons_mean<threshold])

if __name__ == "__main__":

    with open('files/rosalind_bphr.txt', 'r') as fi:
        threshold = int(fi.readline())
        fastq = fi.read()

    with open('tmp.fastq', 'w') as fo:
        fo.write(fastq)

    handle = SeqIO.parse('tmp.fastq', 'fastq')

    # Run the function
    print qphredthreshold(threshold, handle)

    # Remove the temporary file
    os.system('rm tmp.fastq')
