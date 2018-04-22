f,s = 1,1
i = 1
fb = [1,1]

while len(str(f))<1000:
    f,s = f+s,f
    i += 1
    fb.append(f)
print(f,i,len(fb))
