#!/usr/bin/env python3

def divide_genome(genome, L):

    """
    Given a string and an integer L, this function retrieves all the possible L-mers contained in the genome
    """

    m = L
    L_windows = []

    while m <= len(genome):
        new_window = genome[m-L:m]
        L_windows.append(new_window)

        m += 1

    return L_windows


def divide_and_count(L_windows, k, t):

    """
    Given a list of subsequences and k and t, this functions find in each subsequence all the possible k-mers
    appearing exactly t times in the subsequence
    """

    results = set()

    for L_mer in L_windows:
        k_windows = divide_genome(L_mer, k) # We extract in a list all the possible k-mers

        # Generate a set of unique elements to avoid multicounts...
        k_windows_set = set(k_windows)

        for k_window in k_windows_set:
            if k_windows.count(k_window) == t:
                results.add(k_window)


    print("\t".join(results))


if __name__ == "__main__":

    data = [line.strip("\n") for line in open("./files/rosalind_1eba.txt", "r")]

    genome = data[0]
    values = data[1].split()
    k = int(values[0])
    L = int(values[1])
    t = int(values[2])

    windows_list = divide_genome(genome, L)
    divide_and_count(windows_list, k, t)


