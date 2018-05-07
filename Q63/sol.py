cnt = 0
for i in range(1000):
    ix = 1
    st = str(ix**i)
    while len(st)<= i:
        if len(st) == i:
            cnt += 1
        ix += 1
        st = str(ix**i)
print(cnt)
