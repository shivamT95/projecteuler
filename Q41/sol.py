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
l = to_prime(10000000)
def pan(x):
    st = str(x)
    bt = [0 for _ in range(len(st))]
    if '0' in st:
        return False
    for x in st:
        if int(x) > len(st):
            return False
        bt[int(x)-1] =1
    for i in range(len(st)):
        if bt[i] == 0:
            return False
    return True
print(pan(2143))
for x in l:
    if pan(x):
        print(x)
