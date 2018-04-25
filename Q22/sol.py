fo = open("inp.txt",'r')
l = [x[1:-1] for x in fo.readline().split(',')]
l.sort()
a = 0
for i in range(len(l)):
	sc = sum([(ord(c)-ord('A')+1) for c in l[i]])
	a += sc*(i+1)
print(a)
	
