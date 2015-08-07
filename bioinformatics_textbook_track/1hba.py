#!/usr/bin/env python3

def main_f(pattern, genome, d):

    """
    Given a pattern, retrieve the positions in the genome where it appears with less than d mismatches
    """

    approx_match = []

    # Process per len(pattern)-mers generating windows
    for i in range(len(genome)-len(pattern)+1):
        mismatches = 0

        # Process the window base per base counting mismatches
        for j in range(len(pattern)):
            if genome[i:i+len(pattern)][j] != pattern[j]:
                mismatches += 1

        if mismatches <= int(d):
            approx_match.append(str(i))


    print('\t'.join(approx_match))



if __name__ == "__main__":

    data = [line.strip("\n") for line in open("./files/rosalind_1hba.txt", "r")]

    pattern = data[0]
    genome = data[1]
    d = data[2]

    main_f(pattern, genome, d)

