divs = {}
def sm(x):
	s = 0
	for i in range(2,int(x**0.5)):
		if x%i == 0:
			s += i
			s += x/i
			if i*i == x:
				s -= i
	return s+1
for i in range(10001):
	divs[i] = sm(i)
ans = 0
for i in range(10001):
	for j in range(10001):
		if divs[i] == j and divs[j] == i and i!=j:
			ans += i
print(ans)	
