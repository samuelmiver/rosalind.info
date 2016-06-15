#!/usr/bin/env python

from cons import FASTA_iterator

def rc(sequence):
    """Given a string returns the reverse complementary"""

    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(sequence)
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    return(bases)


def hamming_distance(seqA, seqB):
    """Given two string sequences looks for the Hamming distance (number of mismatches)"""

    i = 0
    hmmdist = 0
    while i < len(seqA):
        if seqA[i]!=seqB[i]:
            hmmdist += 1
        i += 1
    return hmmdist


def corr(fasta_file):

    # Iterate to detect duplicates
    all_sequences = [nts for ide, nts in FASTA_iterator(fasta_file)]
    all_sequences += [rc(seq) for seq in all_sequences]

    correct   = []
    incorrect = []

    for seqA in all_sequences[0:len(all_sequences)/2]:
        if all_sequences.count(seqA) == 1:
            incorrect.append(seqA)
        else:
            if seqA not in correct:
                correct.append(seqA)

    correct_rev = [rc(seq) for seq in correct]

    for seqA in incorrect:
        hdist = [hamming_distance(seqA, seqB) for seqB in correct]
        hdist_rev = [hamming_distance(seqA, seqB) for seqB in correct_rev]

        if hdist.count(1) == 1:
            seqB = correct[hdist.index(1)]
            print(seqA+'->'+seqB)
        elif hdist_rev.count(1)==1:
            seqB = correct_rev[hdist_rev.index(1)]
            print(seqA+'->'+seqB)
        else:
            pass


if __name__ == '__main__':
    corr('./files/rosalind_corr.txt')
