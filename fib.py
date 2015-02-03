def fib_rab(number_months,new_rabbits_per_month):
	fib_table = []
	for i in range(number_months):
		if i < 2:
			fib_table.append(1)
		else:
			fib_table.append(fib_table[-1] + fib_table[-2]*new_rabbits_per_month)
	return fib_table

with open('files/rosalind_fib.txt', 'r') as f:
	number_months, new_rabbits_per_month = f.readline().split()
	print fib_rab(int(number_months), int(new_rabbits_per_month))[-1]
