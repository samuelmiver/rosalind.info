#!/usr/bin/env python

from Bio import SeqIO

def fastq2fasta(filename):

    """
    Given a fastq file, returns and print the correspondant fasta
    """

    SeqIO.convert(filename, "fastq", "your_file.fasta", "fasta")


if __name__ == '__main__':
    fastq2fasta('files/rosalind_tfsq.txt')



