with open('files/rosalind_ba1f.txt') as input_data:
	dna = input_data.read().strip()

skew_value, min_skew, min_ind = 0, 1, []
for index, nucleotide in enumerate(dna):
	
	if nucleotide == 'C':
		skew_value -= 1
	elif nucleotide == 'G':
		skew_value += 1
	
	if skew_value == min_skew:
		min_ind.append(str(index+1))
	elif skew_value < min_skew:
		min_skew = skew_value
		min_ind = [str(index+1)]

print ' '.join(min_ind)
