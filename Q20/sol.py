fact = 1
for i in range(1, 101):
	fact = fact*i
ans = 0
while fact != 0:
	ans += (fact % 10)
	fact = fact//10
print(ans)