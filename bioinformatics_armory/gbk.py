#!/usr/bin/env python


import sys
from Bio import Entrez
Entrez.email = "samuel.miravet@crg.eu"

genus, st_date, en_date = map(lambda line: line.strip(), open("files/rosalind_gbk.txt").readlines())
handle = Entrez.esearch(db="nucleotide", term=genus+'[Organism] AND ('+st_date+'[PDAT] : '+en_date+'[PDAT])')
record = Entrez.read(handle)
handle.close()
print int(record["Count"])
