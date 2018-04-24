tns = set([n*(n+1)/2 for n in range(100000)])
pens = set([n*(3*n-1)/2 for n in range(100000)])
hx = [n*(2*n-1) for n in range(100000)]
for x in hx:
    if x in tns and x in pens:
        print(x)
