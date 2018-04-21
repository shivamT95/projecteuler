f = 1
s = 1
an = 0
while f <= 4000000:
	f,s = f+s,f
	if f%2 == 0:
		an += f
print(an)
