#!/usr/bin/env python

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

def revcomp(seq_object):

    return seq_object.reverse_complement()

def rvco():

    list_seq = []
    new_entry = None
    with open('files/rosalind_rvco.txt', 'r') as fi:
        for line in fi:
            if line.startswith('>'):
                if new_entry:
                    list_seq.append(new_entry)
                    new_entry = ''
                else:
                    new_entry = ''
            else:
                new_entry += line.strip()

    # Store the last record
    list_seq.append(new_entry)

    # Counting
    counts = 0
    for sequence in list_seq:
        myseq = Seq(sequence, IUPAC.unambiguous_dna)
        revc = revcomp(myseq)

        if str(myseq) == str(revc):
            counts += 1

    print(counts)





if __name__ == '__main__':
    rvco()


    # One line
    print sum(rec.seq == rec.reverse_complement().seq for rec in SeqIO.parse('files/rosalind_rvco.txt', 'fasta'))

