fac = [1]
for i in range(1,101):
    fac.append(fac[i-1]*i)
cnt = 0
for n in range(1,101):
    for r in range(n):
        ncr = fac[n]/(fac[r]*fac[n-r])
        if ncr > 10**6:
            cnt += 1
print(cnt)
