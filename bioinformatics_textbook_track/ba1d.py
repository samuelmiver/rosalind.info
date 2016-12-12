def pattern_matching(filename):
	"""Given a short string and a whole sequence, retrieve the
	indexes where the submotif appears """

	with open(filename) as filehandle:
		subseq = filehandle.readline().strip()
		seq = filehandle.readline()

	locations = []
	i = seq.find(subseq, 0)
	while i != -1:
		locations.append(i)
		i += 1
		i = seq.find(subseq, i)
	return '%s' % ' '.join(map(str, locations))


print (pattern_matching("./files/rosalind_ba1d.txt"))
