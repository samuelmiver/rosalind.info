#A previous function in order to get the sequences
def FASTA_iterator( fasta_filename ):
	""""A Generator function that reads a FASTA file. In each iteration, the function returns a 
	tuple with the	following format: (identifier, sequence)."""

	fasta_file = open(fasta_filename,'r')
	
	identifier = ""
	completeseq = []

	for line in fasta_file:
		line = line.strip()
		if line.startswith(">"):
			if completeseq:
				yield (identifier, ''.join(completeseq))
				completeseq = []
			identifier = line[1:]
		else:
			completeseq.append(line)

	fasta_file.close()

	if len(''.join(completeseq))>0:
		yield (identifier, ''.join(completeseq))

#Start the function to generate the profile:

def profile_matrix_creator( fasta_filename ):

	'''Given a list of sequences, returns a profile matrix as a dictionary {'A': [5 1 0 0 ..], 'T': [0 0 3 5], 'C': etc.}'''

	seqlist = []
	for identifier, sequence in FASTA_iterator(fasta_filename):
		seqlist.append(sequence)

	#1. First generate an empty hash
	profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
	
	#2. Iterate and generate the counts of each nt for each position
	for item in zip(*seqlist):
		for nt in ['A', 'C', 'G', 'T']:
			profile_matrix[nt].append(item.count(nt))
	
	return profile_matrix

#And the function to generate the consensus:

def consensus_string( profile_matrix ):
	'''This function returns a consensus string (a sequence for example) from a profile matrix'''
	
	consensus_seq = ''
	elements = tuple(profile_matrix.items())		#the method functions retrieve a list of tuples from a dictionary
	length = len(elements[0][1])
	for i in range(length):
		consensus_seq += max(elements, key = (lambda x: x[1][i]))[0]
	
	return consensus_seq


#Execution part:
x = profile_matrix_creator("./rosalind_cons.txt")
y = consensus_string(x)

print (y)
for element in x:
    print (element+':'," ".join([str(num) for num in x[element]]))
