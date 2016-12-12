#!/usr/bin/env python

import utils

def revcomp(s):
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([comp[c] for c in reversed(s)])

def reverse_palindromes(s):
    results = []
    l = len(s)
    for i in range(l):
        for j in range(4, 13):
            if i + j > l:
                continue
            s1 = s[i:i+j]
            s2 = revcomp(s1)
            if s1 == s2:
                results.append((i + 1, j))
    return results

if __name__ == "__main__":

    seq = utils.load_multifasta('files/rosalind_revp.txt').values()[0]
    results = reverse_palindromes(seq)
print "\n".join([' '.join(map(str, r)) for r in results])
