#!/usr/bin/env python3

def main_f(peptide, genomei, codon_table):

    """
    Given a peptide, retrieve the sequences in the genome codifying it (6 ORFs)
    """

    len_codingseq = 3*len(peptide)

    ORFs = [0, 1, 2]

    # Prepare the reverse complementary genome:
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

    def reverse_complement(seq):
        for k,v in alt_map.iteritems():
            seq = seq.replace(k,v)

        bases = list(seq) 
        bases = reversed([complement.get(base,base) for base in bases])
        bases = ''.join(bases)

        return bases

    rev_genome = reverse_complement(genome)

    genomes = [genome, rev_genome]

    for sequence in genomes:
        for i in ORFs:
            codon_start = i
            while codon_start <= len(sequence)-3:
                coding_sequence = sequence[i:i+3]
                tranlated_sequence = coding_sequence.replace

                codond_start += 3







    print(' '.join(results))


if __name__ == "__main__":
    codon_table = {
        'A': ('GCT', 'GCC', 'GCA', 'GCG'),
        'C': ('TGT', 'TGC'),
        'D': ('GAT', 'GAC'),
        'E': ('GAA', 'GAG'),
        'F': ('TTT', 'TTC'),
        'G': ('GGT', 'GGC', 'GGA', 'GGG'),
        'I': ('ATT', 'ATC', 'ATA'),
        'H': ('CAT', 'CAC'),
        'K': ('AAA', 'AAG'),
        'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
        'M': ('ATG',),
        'N': ('AAT', 'AAC'),
        'P': ('CCT', 'CCC', 'CCA', 'CCG'),
        'Q': ('CAA', 'CAG'),
        'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
        'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
        'T': ('ACT', 'ACC', 'ACA', 'ACG'),
        'V': ('GTT', 'GTC', 'GTA', 'GTG'),
        'W': ('TGG',),
        'Y': ('TAT', 'TAC'),
        '*': ('TAA', 'TAG', 'TGA'),
    }

    genome = data[0]
    peptide = data[1]

    main_f(peptide, genome, codon_table)

