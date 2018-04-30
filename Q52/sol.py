def same_dit(l):
    bt = [0 for _ in range(10)]
    for x in str(l[0]):
        bt[int(x)] += 1
    for n in l[1:]:
        btt = [0 for _ in range(10)]
        for x in str(n):
            btt[int(x)] += 1
        for i in range(10):
            if bt[i] != btt[i]:
                return False
    return True
x = 1
while(True):
    l = [i*x for i in range(1,7)]
    if same_dit(l):
        print(l)
        break
    x += 1
