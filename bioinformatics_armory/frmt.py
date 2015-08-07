#/usr/bin/env python3

from Bio import Entrez
from Bio import SeqIO

def frmt(filename):
    """
    A collection of n (n≤10) GenBank entry IDs, it returns the shortest of the strings associated with the IDs in FASTA format
    """

    # Open the file
    with open(filename) as input_data:
        IDs = input_data.read().strip().split()

    # SOme requirements to handle the file
    Entrez.email = 'samuelmiver@hotmail.com'
    handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))

    # Find the minimal index
    [min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]

    alt_handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
    FASTA = alt_handle.read().strip().split('\n\n')[min_index]

    print(FASTA)

if __name__ == '__main__':
    frmt('files/rosalind_frmt.txt')
