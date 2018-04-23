sol_set = set()
for a in range(2,101):
	for b in range(2,101):
		sol_set.add(a**b)
print(len(sol_set))