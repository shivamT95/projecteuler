def check(n):
	if(n < 100000000 or n > 999999999):
		return False
	st = set()
	while(n):
		st.add(n%10)
		n = n//10
	return (len(st) == 9 and (0 not in st))
ans = -1
for n in range(2,10):
	for i in xrange(1,10000000000):
		pdt = ""
		for j in range (1,n+1):
			pdt = pdt+str(i*j)
		pdt = int(pdt)
		if(pdt > 999999999):
			break
		if(check(pdt)):
			ans = max(ans,pdt)
print(ans)
