l = [1,2,5,10,20,50,100,200]
mem = {}
def ways(n):
    tb = [0 for k in range(n+1)]
    tb[0]= 1
    for x in l:
        for j in range(x,n+1):
            tb[j] += tb[j-x]
    return tb[n]
print(ways(200))
