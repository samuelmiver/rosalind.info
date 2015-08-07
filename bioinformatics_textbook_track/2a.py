def translate(filename):
	"""Translates a RNA string to protein"""

	start_codons = ['UUG', 'CUG', 'AUG']
	stop_codons = ['UAA', 'UAG', 'UGA']
	aa_table = {'GUC': 'V', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GUU': 'V', 'AAC': 'N', 
				'AGG': 'R', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'AGA': 'R', 'AAU': 'N', 
				'ACU': 'T', 'CAC': 'H', 'GUG': 'V', 'CCG': 'P', 'CCA': 'P', 'AGU': 'S', 
				'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 
				'CGC': 'R', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 
				'GGA': 'G', 'GGC': 'G', 'GAG': 'E', 'UCC': 'S', 'UAC': 'Y', 'CGU': 'R', 
				'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 
				'CUG': 'L', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 
				'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'UGC': 'C', 
				'GCU': 'A', 'UGU': 'C', 'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 
				'UUC': 'F'}

	your_file = open(filename,'r')

	for line in your_file:
		line = line.strip()
		sequence = line

	your_file.close()


	protein_result = []
	searching_start = True
	s = 0
	t = 2 		#t and s are two variables needed to change the behavior of the loop

	for nt in range(0, len(sequence) - 2, 1):
		nt += s
		codon = sequence[nt:nt+3]
		if len(codon) < 3:
			break

		if not searching_start and codon not in stop_codons:
			protein_result.append(aa_table[codon])
			s += t
		elif not searching_start and codon in stop_codons:
			break
		elif searching_start and codon in start_codons:
			searching_start = False
			protein_result.append(aa_table[codon])
			s = 2

	#Defining the result as a new Protein object
	if not searching_start and codon in stop_codons :
		return ''.join(protein_result)
	elif not searching_start and codon not in stop_codons:
		return ''.join(protein_result)

	#Some control advises:
	if searching_start:
		print ("Your sequence has no start codons")


# Paste here the RNA to translate
print (translate("files/rosalind_2a.txt"))
