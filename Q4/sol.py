mx = 0
for x in range(100,1000):
	for y in range(100,1000):
		pr = x*y
		if str(pr) == str(pr)[::-1]:
			if pr>mx:
				mx = pr
print(mx)
