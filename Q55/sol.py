cnt = 0
l = []
for x in range(1,10001):
    it = 55
    f =0
    ox = x

    rev = int(str(x)[::-1])
    x += rev
    while it>=0 :
        rev = int(str(x)[::-1])
        if x == rev:
            f = 1
            break
        x = x + rev
        it -= 1
    if f == 0:
        l.append(ox)
        cnt +=1
print(l,len(l))
