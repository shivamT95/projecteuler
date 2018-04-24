import math
def is_prime(n):
	if n == 1:
		return False
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n))+1,2))
def check(n):
	tn = n
	tp = 1
	while(n != 0):
		if(is_prime(n) == False):
			return False
		n = n//10
		tp = tp*10
	while(tn != 0):
		if(is_prime(tn) == False):
			return False
		tn = tn % tp
		tp = tp//10
	return True
ans = 0
for i in range(11,1000000):
	if(is_prime(i)):
		if(check(i)):
			ans = ans+i
print(ans)
