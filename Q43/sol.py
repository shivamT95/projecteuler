from itertools import permutations
perm = list(permutations("0123456789"))
def tst(x):
    if int(x[1]+x[2]+x[3])%2 !=0:
        return False

    if int(x[4]+x[2]+x[3])%3 !=0:
        return False

    if int(x[3]+x[4]+x[5])%5 !=0:
        return False

    if int(x[4]+x[5]+x[6])%7 !=0:
        return False

    if int(x[5]+x[6]+x[7])%11 !=0:
        return False

    if int(x[6]+x[7]+x[8])%13 !=0:
        return False

    if int(x[7]+x[8]+x[9])%17 !=0:
        return False
    return True
sm = 0
for t in perm:
    if tst(t):
        sx = ""
        for x in t:
            sx += x
        print(sx)
        sm += int(sx)
print(sm)
