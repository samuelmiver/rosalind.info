def reverse_complement(filename):
    """Given a string returns the reverse complementary"""

    with open(filename) as filehandle:
        seq = filehandle.readline().strip()

    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    print(bases)


reverse_complement("./files/rosalind_ba_1c.txt")
