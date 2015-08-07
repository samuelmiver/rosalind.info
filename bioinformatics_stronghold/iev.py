#!/usr/bin/env python3


def iev(filename):
    """
    Given six positive integers, each of which does not exceed 20,000. The integers correspond
    to the number of couples in a population possessing each genotype pairing for a given
    factor. In order, the six given integers represent the number of couples having the
    following genotypes.

    Return The expected number of offspring displaying the dominant phenotype in the next
    generation, under the assumption that every couple has exactly two offspring.
    """

    # Open the file:

    with open(filename) as inFile:
        s = inFile.read().split()

    # Define a probability of dominance for each genotype pairing (AAxAA, AAxAa...)

    prob_list = [1, 1, 1, 0.75, 0.5, 0]

    # Iterate and do the summatory:
    expectedvalues = []
    for index, parents in enumerate(s):
        expectedvalues.append(2*int(parents)*prob_list[index])

    # Return the result:
    return sum(expectedvalues)


if __name__ == '__main__':
    print(iev('files/rosalind_iev.txt'))
