import math
#replace with sieve for faster check, but expected small answer
def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))

primes = []
for i in range(1,1000000):
	if is_prime(i):
		primes.append(i)

def check(k):
	sm = 0
	for i in range(k):
		sm = sm+primes[i]
	if(sm > 1000000):
		return False
	if(sm in primes):
		print(sm)
		return True
	for i in range(k,len(primes)):
		sm = sm-primes[i-k]
		sm = sm+primes[i]
		if(sm > 1000000):
			return False
		if(sm in primes):
			print(sm)
			return True
	return False

for i in range(1000,21,-1):
	if(check(i)):
		break
