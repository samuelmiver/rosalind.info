#!/usr/bin/env python 

from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC
from re import finditer


def longest_orf():
    """
    Given a sequence returns the maximal length protein given translating it (direct and reverse)
    """

    sequence = ''
    with open('files/rosalind_orfr.txt') as fi:
        sequence = Seq(fi.read().rstrip(), IUPAC.unambiguous_dna)

    coding_sequences = [sequence, sequence.reverse_complement()]

    longest = None
    for i in range(3):
        for dna in coding_sequences:
            trans = translate(dna[i:], to_stop=True)
            if not longest or len(longest) < len(trans):
                longest = trans


    for sequence in coding_sequences:
        # Get the starting position for each ORF in the dna sequence and translate.
        ORFs = [translate(dna[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna))]
        # Get the starting position for each ORF in the reverse complement sequence and translate.
        ORFs += [translate(dna.reverse_complement()[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna.reverse_complement()))]

        # Find the longest ORF.
        longest_orf = max(map(str, ORFs), key=len)

    # Print:
    if len(longest_orf) > len(longest):
        print longest_orf
    else:
        print longest

if __name__ == '__main__':
    longest_orf()

