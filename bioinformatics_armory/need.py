#!/usr/bin/env python
# encoding: utf-8

import os

from Bio.Emboss.Applications import NeedleCommandline
from Bio import SeqIO, Entrez

def need():
    """
    Given two genbank IDs, returns the maximum glabl alignment score between the DNA strings associated with these IDs
    """

    # Open th file
    with open('files/rosalind_need.txt') as fi:
        ids = fi.read().split()

    Entrez.email = "samuelmiver@hotmail.com"
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype="fasta")
    records = list(SeqIO.parse(handle, 'fasta'))

    for i, r in enumerate(records):
        with open(ids[i], 'w') as f:
            SeqIO.write(r, f, 'fasta')

    needle_cline = NeedleCommandline()
    needle_cline.asequence = ids[0]
    needle_cline.bsequence = ids[1]
    needle_cline.outfile = "need.txt"
    needle_cline.gapopen = 11
    needle_cline.gapextend = 1
    needle_cline.endopen = 11
    needle_cline.endextend = 1
    needle_cline.endweight = True

    needle_cline()

    with open('need.txt') as f:
        output = f.readlines()

    for line in output:
        if 'Score:' in line:
            print(int(float(line[:-1].split(':')[-1].strip())))

if __name__ == '__main__':
    need()
