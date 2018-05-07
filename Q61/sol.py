tr = [n*(n+1)/2 for n in range(205)]
sq = [n*n for n in range(105)]
pt = [n*(3*n-1)/2 for n in range(105)]
hx = [n*(2*n-1) for n in range(105)]
hep = [n*(5*n-3)/2 for n in range(105)]
ot = [n*(3*n-2) for n in range(105)]
tr = filter(lambda x: len(str(x))==4,tr)
sq = filter(lambda x: len(str(x))==4,sq)
pt = filter(lambda x: len(str(x))==4,pt)
hx = filter(lambda x: len(str(x))==4,hx)
hep = filter(lambda x: len(str(x))==4,hep)
ot = filter(lambda x: len(str(x))==4,ot)

if 8128 in tr:
    if 8281 in sq:
        if 2882 in pt:
            print("hoo")
def cyc(x,st,cur,sol):
    if len(cur) == 0:
        if str(st)[:2] == str(x)[2:]:
            print(sol,sum(sol))
        return

    for i in range(len(cur)):
        for y in cur[i]:
            if str(x)[2:] == str(y)[:2]:
                sol.append(y)
                cyc(y,st,cur[:i]+cur[i+1:],sol)
                sol.pop()
for x in tr:
    cyc(x,x,[sq,pt,hx,hep,ot],[x])

