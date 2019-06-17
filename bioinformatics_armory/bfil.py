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
    trimming_seq = []
    for record in handle:
        qual = np.array(record.letter_annotations["phred_quality"])
        binq = qual>=threshold
        binq = list(binq.astype(np.int))
        l = len(binq)
        st = binq.index(1)
        en = binq[::-1].index(1)
        trimming_seq += [[0,l], [st, l-en], [0,l], [st, l-en]]
    return trimming_seq

if __name__ == "__main__":

    with open('files/rosalind_bfil.txt', 'r') as fi:
        threshold = int(fi.readline())
        fastq = fi.read()

    with open('tmp.fastq', 'w') as fo:
        fo.write(fastq)

    handle = SeqIO.parse('tmp.fastq', 'fastq')
    # Run the function
    trimming_array = qphredthreshold(threshold, handle)

    with open('tmp.fastq', 'r') as fi:
        for line, indexes in zip(fi, trimming_array):
            line = line.strip()
            st, en = indexes
            print line[st:en]
    # Remove the temporary file
    os.system('rm tmp.fastq')
