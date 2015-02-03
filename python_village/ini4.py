# Problem
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

def function (x, y):
	a = 0
	while x != y:
		x = x + 1
		if x % 2 == 1:
			a = x + a
	return a

b = function (4994,9496)

print (b)