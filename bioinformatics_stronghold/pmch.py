import utils as u
import sys
from math import factorial

def pmch(fil=False):
    """ Fil = file with the string """
    if not fil:
        seqs = u.load_multifasta('/home/smiravet/sam_things/rosalind.info/bioinformatics_stronghold/files/rosalind_pmch.txt')
    seq = seqs.values()[0]    
    return factorial(seq.count('A'))*factorial(seq.count('G'))

pmch(sys.argv[1])
