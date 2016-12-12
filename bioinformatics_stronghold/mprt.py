#!/usr/bin/env python

import sys
import re
import urllib2


def mprt():

    # parse the file
    IDs = []
    with open('./files/rosalind_mprt.txt', 'rU') as fi:
        for line in fi:
            IDs.append(line.strip())

    # Iteratively download the fasta and look for motives
    url = 'http://www.uniprot.org/uniprot/%s.fasta'
    motif = re.compile('N[^P](S|T)[^P]')
    for ide in IDs:
        fasta = urllib2.urlopen(url % ide)
        fasta.readline()
        seq   = fasta.read().replace('\n','')

        matched_motifs = motif.finditer(seq)
        positions = [str(n+1) for n in range(len(seq)) if motif.match(seq[n:n+4])]
        if positions:
            print ide
            print ' '.join(positions)

if __name__ == '__main__':
    mprt()
