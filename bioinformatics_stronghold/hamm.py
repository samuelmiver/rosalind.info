#!/usr/bin/env python


def SNP_counter(my_list):
    """Given two sequences in a txt file it looks for the Hamming distance (number of mismatches)"""
    i = 0
    hmmdist = 0
    while i < len(my_list[0]):
        if my_list[0][i]!=my_list[1][i]:
            hmmdist += 1
        i += 1
    return hmmdist


if __name__ == '__main__':
    with open("./files/rosalind_hamm.txt", 'r') as infile:
        data = infile.read()
        my_seqs = data.splitlines()
    print SNP_counter(my_seqs)
