import math

def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))

tot = 1
dia = 0
for side_length in range(3,100001,2):
	hi = side_length**2
	for i in range(4):
		if is_prime(hi-i*side_length+i):
			dia = dia+1
	tot = tot+4
	if dia/tot < 0.1:
		print(side_length)
		break
