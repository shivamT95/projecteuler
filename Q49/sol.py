import math
from itertools import permutations
#replace with sieve for faster check, but expected small answer
def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))
primes = []
perms = {}
for i in range(1000,10000):
	if is_prime(i):
		primes.append(i)
		perms[i] = [''.join(p) for p in permutations(str(i))]
for i in primes:
	j = i+3330
	k = j+3330
	if (j not in primes) or (k not in primes):
		continue
	if (str(j) not in perms[i]) or (str(k) not in perms[i]):
		continue
	print(str(i)+str(j)+str(k))

