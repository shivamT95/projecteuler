import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

product = 0
ans = -1

for a in range(-1000,1001):
	for b in range(-1000, 1001):
		tmp = 0
		while True:
			if(is_prime(tmp*tmp + a*tmp + b) == False):
				break
			tmp = tmp+1
		if(tmp > ans):
			ans = tmp
			product = a*b

print(product)