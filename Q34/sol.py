def fac(x):
    p = 1
    for i in range(1,x+1):
        p *=i
    return p
fc = [fac(x) for x in range(10)]
print(fc)
sm = 0
for i in range(10,fac(9)):
    s = 0
    for x in str(i):
        s += fc[int(x)]
    if s == i:
        print(i)
        sm += i
print(sm)
