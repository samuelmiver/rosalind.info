#!/usr/bin/env python

def mrna(protein):
    poscodons = {'A': 4,'C': 2,'D': 2,'E': 2,'F': 2,'G': 4,'H': 2,'I': 3,'K': 2,'L': 6,'M': 1,'N': 2,'P': 4,'Q': 2,'R': 6,'S': 6,'T': 4,'V': 4,'W': 1,'Y': 2}
    possible_rna = 1
    for aminoacid in protein:
        possible_rna *= poscodons[aminoacid]

    return 3*possible_rna % 1000000

if __name__ == '__main__':

    with open('files/rosalind_mrna.txt','r') as fi:
        for line in fi:
            aa_seq = line.strip()


    print mrna(aa_seq)
