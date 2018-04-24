lt = [i*(i+1)/2 for i in range(10000)]
s = raw_input().split(',')
st = [x[1:-1] for x in s]
print(st)
cnt = 0
for w in st:
    sc = 0
    for l in w:
        sc += ord(l)-ord('A')+1
    if sc in lt:
        cnt += 1
print(cnt)
