n = 1000000
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
def valr(x):
    sx = str(x)
    for x in sx:
        if int(x)%2 == 0:
            return False
    for i in range(1,len(sx)):
        s = sx[i:] + sx[:i]
        if int(s) not in l:
            return False
    return True
cnt = 0
for x in l:
    if valr(x)==True:
        cnt += 1
        print(x,cnt)
print(cnt+1) # 2 mssing from solution
