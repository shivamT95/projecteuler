n = 2000000
def to_prime(m):
	bt = [False for _ in range(int(m+1))]
	for x in range(2,int(m**0.5)):
		if bt[x] == False:
			j = x*x
			while j <= m:
				bt[j] = True
				j += x
	pr = []
	for x in range(2,int(m+1)):
		if bt[x] == False:
			pr.append(x)
	return pr
		
a = 1
l = to_prime(n)
print(sum(l))
