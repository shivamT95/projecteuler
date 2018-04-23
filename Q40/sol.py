sol = ""
for i in range (1,1000000):
	sol = sol+str(i)
	if len(sol) > 1000000:
		break
ans = 1
for i in range(6):
	ans = ans*int(sol[10**i-1])
print(ans)