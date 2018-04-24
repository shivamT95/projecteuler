def isPalin(str):
	return str == str[::-1]
ans = 0
for i in range(1000000):
	b2 = ""
	tmp = i
	while(tmp):
		b2 = str(tmp & 1) + b2
		tmp = tmp//2
	if(isPalin(str(i)) and isPalin(b2)):
		ans = ans+i
print(ans)