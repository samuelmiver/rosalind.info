#!/usr/bin/env python

import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq

# Open the file and take the sequence

handle = open('files/rosalind_orf.txt','r')

for record in SeqIO.parse(handle, "fasta"):
    s= record.seq
handle.close()

sr = s.reverse_complement()
ss = [s, s[1:-2], s[2:-1], sr, sr[1:-2], sr[2:-1]]
prots = set()
for s in ss:
   prots.update((mo.groups()[0][:-1] for mo in re.finditer(r'(?=(M\w*\*))',  str(s.translate())) if mo))

print '\n'.join(prots)
