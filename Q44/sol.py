penl = [n*(3*n-1)/2 for n in range(1,10000)]
pens = set(penl)
f = 0
for d in penl:
    for i in range(10000-1):
        if (d+penl[i]) in pens and (d+2*penl[i]) in pens:
            print(d,penl[i],d+2*penl[i])
            f = 1
            break
    if f == 1:
        break

