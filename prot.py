def RNA2prot(handle):
    """Decode RNA into protein sequence"""

    # Create a dictionary of amino acid codes
    aamap = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    # Read in file
    f = open(handle, 'r')
    mRNA = f.readline()

    protein = []
    for codon in rnareader(mRNA):

        if aamap[codon] == "STOP":
            break
        
        if codon == "AUG":
            start = True

        if start:
            if aamap[codon] == "STOP":
                break
            aa = aamap[codon]
            protein.append(aa)


    print ''.join(protein)
                
# Also need to build a generator to return
def rnareader(rnastr):
    aacodon = []
    for nuc in rnastr:
        aacodon.append(nuc)
        if len(aacodon) >= 3:
            yield ''.join(aacodon)
            aacodon = []


RNA2prot("./files/rosalind_prot.txt")