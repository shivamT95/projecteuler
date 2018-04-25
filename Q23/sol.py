divs = {}
def sm(x):
	s = 0
	for i in range(2,int(x**0.5)+1):
		if x%i == 0:
			s += i
			s += x/i
			if i*i == x:
				s -= i
	return s+1
ans = 0
ab = {}
n = 28124
for i in range(1,28124):
	if sm(i)>i:
		ab[i] = 1
for i in range(1,n+1):
	f = 0
	for j in ab.keys():
		if j>= i:
			break
		if (i-j) in ab:
			f = 1
	if f == 0:
		ans += i	
print(ans)	
