def digsum(n):
	ans = 0
	while n > 0:
		ans = ans + (n % 10)
		n = n//10
	return ans

val = -1
for a in range(1,100):
	for b in range(1,100):
		val = max(val, digsum(a**b))
print(val)