#!/usr/bin/env python

import math

def independent_alleles():
    """
    Solution for the problem of independent alleles presented by Rosalind.info
    """

    with open('files/rosalind_lia.txt', 'r') as fi:
        for line in fi:
            line = line.strip().split()
            k = int(line[0])
            N = int(line[1])

    # A inner function
    def bin_coeff(m, n):
        return math.factorial(m) / (math.factorial(n) * math.factorial(m-n))

    # Compute the probability

    probabilities = 0
    generation_growth = 2**k

    for i in range(N):
        new_probability = bin_coeff(generation_growth, i) * 0.25**i * 0.75**(generation_growth - i)
        probabilities += new_probability

    print 1 - probabilities


if __name__ == '__main__':
    independent_alleles()
