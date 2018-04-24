import math
#replace with sieve for faster check, but expected small answer
def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))
primes = []
for i in range(1,10000):
	if is_prime(i):
		primes.append(i)
ans = 10000000
sols = set()
for i in range(1,1000):
	for p in primes:
		oc = 2*i*i+p
		if oc & 1 == 1 and is_prime(oc) == False:
			sols.add(oc)
for i in range(9,1000000,2):
	if(is_prime(i)):
		continue
	if i not in sols:
		ans = i
		break
print(ans)
