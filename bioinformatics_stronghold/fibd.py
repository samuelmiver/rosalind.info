def fibd(filename):
	"""Given a file with two integers, the function solves
	the problem of "Mortal Fibonacci Rabbits presented at 
	rosalind.info

	"""
	
	with open (filename) as input_data:
		n,m = map(int, input_data.read().split())

	# Initial rabbit population:

	rabbits = [1]+[0]*(m-1)

	# Calculate new rabbits in a given year (start the 
	# year in 1 sinc eour initial population is in year 0:

	for year in range(1, n):
		new_rabbits = 0

		# Get number of rabbits able to get new rabbits:
		for j in range(1, m):
			new_rabbits += rabbits[(year-j-1)%m]

		# replacing old bunnies:
		rabbits[(year)%m] = new_rabbits

	total_rabbits = sum(rabbits)

	# Output:
	print (total_rabbits)

#Execution part
fibd("./files/rosalind_fibd.txt")