ways = [[-1]*100 for _ in range(100)]
ways[0][0] = 1
def waysr(n,m):
	if n<0 or m <0:
		return 0
	if ways[n][m] != -1:
		return ways[n][m]
	if n == 0 and m == 0:
		return 1
	ways[n][m] = waysr(n-1,m)+waysr(n,m-1)
	return ways[n][m]
print(waysr(20,20))
