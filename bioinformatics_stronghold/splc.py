#!/usr/bin/env python

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC

def translate_dna(dna):
    """
    Return protein sequence using given DNA sequence and NCBI table code
    """
    return translate(dna, stop_symbol="")

def splc(fasta_file):


    l = [x.seq for x in SeqIO.parse(open(fasta_file, 'r'), "fasta")]
    original, introns = str(l[0].transcribe()), [str(s.transcribe()) for s in l[1:]]

    for intron in introns:
        original = original.replace(intron, '')

    print Seq(original, IUPAC.unambiguous_rna).translate(to_stop=True)

if __name__ == '__main__':
    splc('./files/rosalind_splc.txt')
