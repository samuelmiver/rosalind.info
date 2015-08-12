#!/usr/bin/env python

from Bio import SeqIO
import statistics as stat
import sys
import os

def qphredthreshold(threshold,handle):
    """
    Given a threshold and a FastQ file, prints the number of sequences with quality over the threshold value
    """

    counts = 0
    for record in handle:
        if stat.mean(record.letter_annotations["phred_quality"]) < int(threshold):
            counts += 1

    print(counts)

    return counts


if __name__ == "__main__":

    # process thefile to extract the threshold and generate the fastq file

    fastq_outfile = open("tmp_fastq.fastq", "w")

    with open('files/rosalind_phre.txt', 'r') as fi:
        threshold = int(fi.readline())
        fastq = fi.read()

    with open('tmp.fastq', 'w') as fo:
        fo.write(fastq)

    handle = SeqIO.parse('tmp.fastq', 'fastq')

    # Run the function
    qphredthreshold(threshold, handle)

    # Remove the temporary file
    os.system('rm tmp.fastq')
