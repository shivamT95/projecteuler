def pan(a,b,c):
    s = str(a)+str(b)+str(c)
    if len(s) != 9 or '0' in s:
        return False
    bt = [0 for x in range(9)]
    for x in s:
        bt[int(x)-1] = 1
    for x in range(9):
        if bt[x] == 0:
            return False
    return True
a = {}
for i in range(20000):
    if pan(2,i,2*i):
        print(i)
for i in range(5000):
    for j in range(5000):
        if pan(i,j,i*j):
            print(i,j,i*j)
            a[i*j] = 1
print(sum(a.keys()))
