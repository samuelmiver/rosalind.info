#!/usr/bin/env python3

from Bio.Seq import Seq

def nt_counter(filename):
    """
    Given a sequence in a filename it returns the counts for each nucleotide A, C, G and T
    """

    with open(filename) as fi:
        for line in fi:
            sequence = line.strip()

    # Use Biopython to count

    my_seq = Seq(sequence)

    print(my_seq.count('A'), my_seq.count('C'), my_seq.count('G'), my_seq.count('T'))


if __name__ == '__main__':
    nt_counter('files/rosalind_ini.txt')
