import math
sols = {}
for i in range(1001):
	sols[i] = 0
for a in range(1, 1000):
	for b in range(1, 1000):
		c = int(math.sqrt(a*a + b*b))
		if(a*a + b*b == c*c and a+b+c < 1001):
			sols[a+b+c] = sols[a+b+c]+1
nsol = -1
ans = -1
for i in range(1001):
	if(sols[i] > nsol):
		ans = i
		nsol = sols[i]
print(ans)