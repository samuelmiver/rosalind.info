def SNP_counter(filename):
	"""Given two sequences in a txt file it looks for the Hamming distance (number of mismatches)"""

	#First we open the file and create a list where each line is our sequence:

	with open(filename, 'r') as infile:
		data = infile.read()

	my_list = data.splitlines()

	#my_list[0] will be the first line for example.

	#And we compare character by character the using a loop

	i = 0
	hmmdist = 0
	while i < len(my_list[0]):
		if my_list[0][i]!=my_list[1][i]:
			hmmdist += 1
		i += 1

	print hmmdist


SNP_counter("./files/rosalind_ba1g.txt")
