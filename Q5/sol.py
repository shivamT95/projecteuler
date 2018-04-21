def hcf(a,b):
	if b== 0:
		return a
	return hcf(b,a%b)

pr = 1
for x in range(2,21):
	h = hcf(pr,x)
	pr = pr*x
	pr = pr/h
	print(pr)
