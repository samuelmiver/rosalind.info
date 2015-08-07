#!/usr/bin/env python3

from Bio import ExPASy
from Bio import SwissProt

def bio_processes(protID, printer=False):
    """
    Given a protein ID, this function returns all the functions listed in uniprot for it.

    This function makes use of the ExPASy package from biopython

    If printer, the function will show in cmd the results, if not, it just returns a list of strings
    with the correspondant functions
    """

    handle = ExPASy.get_sprot_raw(protID)
    record = SwissProt.read(handle)

    # Generate a list with the functions:
    functions = []

    for entry in record.cross_references:
        if entry[0] == 'GO' and entry[2][0] == 'P':
            functions.append(entry[2].lstrip('P:'))

    # Print the result
    if printer:
        print('\n'.join(functions))

    # Return the list
    return functions

if __name__ == '__main__':

    with open('files/rosalind_dbpr.txt') as fi:
        for line in fi:
            protID = line.strip()

    result = bio_processes(protID, printer=True)
