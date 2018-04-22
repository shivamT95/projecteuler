def tg(x):
	return x*(x+1)/2
def div_cnt(x):
	c = 0
	for i in range(1,int(x**0.5)):
		if x%i == 0:
			c += 2
			if i*i == x:
				c -= 1
	return c	
i = 1
while div_cnt(tg(i)) <= 500:
	i += 1
print(tg(i))
