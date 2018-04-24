import math
#replace with sieve for faster check, but expected small answer
def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))

primes = []
for i in range(1,100000):
	if is_prime(i):
		primes.append(i)
def dpf(n):
	tn = n
	ans = 0
	for p in primes:
		flag = 0
		while n % p == 0:
			flag = 1
			n = n/p
		ans = ans+flag
		if p*p > tn:
			break
	if n != 1:
		ans = ans+1
	return (ans==4)

for i in range(1,1000000):
	if dpf(i) and dpf(i+1) and dpf(i+2) and dpf(i+3):
		print(i)
		break

