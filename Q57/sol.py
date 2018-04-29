import math

val = 0
lv = 1,2
for i in range(1,1001):
	lv1 = int(math.log10(lv[0]+lv[1]))
	lv2 = int(math.log10(lv[1]))
	#print(lv[0]+lv[1], lv[1], lv1, lv2)
	if(lv1 > lv2):
		val = val+1
	lv = lv[1],lv[1]*2+lv[0]

print(val)
