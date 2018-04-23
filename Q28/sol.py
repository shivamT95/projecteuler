ans = 1
nsf = 1

for i in range(1,501):
	nsf += 8*i
	ans += 4*nsf-12*i
	
print(ans)

