#!/usr/bin/env python


# Extract all the sequences and locathe in an array:
from Bio import SeqIO

seqs = []

handle = open("files/rosalind_long.txt", "rU")
for record in SeqIO.parse(handle, "fasta"):
    seqs.append(str(record.seq))
handle.close()


def loong(seqs, superstr=''):
    """
    Given DNA strings of equal length, return the shortest superstring containing all the given string
    """

    if len(seqs) == 0:
        # This will happen when all the sequences included in the superstring
        return superstr

    elif len(superstr) == 0:
        superstr = seqs.pop(0)
        return loong(seqs, superstr)

    else:
        for i in range(len(seqs)):
            a = seqs[i]
            l = len(a)

            for p in range(l/2):
                q = l-p

                if superstr.startswith(a[p:]):
                    seqs.pop(i)
                    return loong(seqs, a[:p] + superstr)

                if superstr.endswith(a[:q]):
                    seqs.pop(i)
                    return loong(seqs, superstr + a[q:])


print(loong(seqs))


