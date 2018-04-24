ans = 0
for i in range(1,1001):
	ans = ans + pow(i,i,10000000000)
print(ans % 10000000000)
