#!/usr/bin/env python
# encoding: utf-8

import subprocess

def meme(fastafile, printer=False):
    """
    Given: A set of protein strings in FASTA format that share some motif with minimum length 20.
    Return: Regular expression for the best-scoring motif.

    ¡MEME Suite (http://meme.nbcr.net/meme/) is required to run this code!
    """

    # Run the MEME over the file and extract the motif
    cmd = ['meme', fastafile, '-text', '-minw', '20']
    process = subprocess.Popen(cmd, stdout = subprocess.PIPE)

    motif, err = process.communicate()

    # Extract the motif by regexps
    def extract_regex(motivo):
        count = 0
        motif_list = motivo.split('\n')

        for result in motif_list:
            if 'regular expression' in result:
                return motif_list[count + 2]
            count += 1

    # Show results:
    result_motif = extract_regex(motif)

    if printer:
        print(result_motif)
    else:
        return result_motif

if __name__ == '__main__':
    meme('files/rosalind_meme.txt', printer=True)

