ans = 0
for i in range(2,10000000):
	tmp = i
	sm = 0
	while tmp != 0:
		dig = tmp % 10
		sm = sm + (dig**5)
		tmp = tmp//10
	if(sm == i):
		ans = ans + i
print(ans)
