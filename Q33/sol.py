def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def rd(i,x):
    n = ""
    for l in str(i):
        if l != str(x):
            n += l
    if n == "":
        return x
    return int(n)
a= {}
for i in range(10,100):
    for j in range(i+1,100):
        for x in range(1,10):
            if str(x) in str(i) and str(x) in str(j):
                if rd(j,x)!= 0 and rd(i,x)/float(rd(j,x)) == (i/float(j)):
                    print(i,j,rd(i,x),rd(j,x))
                    a[(rd(i,x),rd(j,x))] = 1
pr1,pr2 = 1,1
for x in a.keys():
    pr1,pr2 = pr1*x[0],pr2*x[1]
    print(pr1,pr2,pr2/(gcd(pr1,pr2)))
