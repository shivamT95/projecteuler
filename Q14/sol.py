mp = {}
def c_len(x,l):
	if x in mp:
		return mp[x]+l-1
	if x == 1:
		return l
	if x%2 == 0:
		return c_len(x/2,l+1)
	else:
		return c_len(3*x+1,l+1)
print(c_len(13,1))
i = 1
mx = 1
while i<=1000000:
	v = c_len(i,1)
	mp[i] = v
	if v>c_len(mx,1):
		mx = i
	i += 1
	if i%100==0:
		print(i,v)
print(mx)
