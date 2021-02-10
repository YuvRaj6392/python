n=int(input())
lst=list()
t=list()
z=list()
if n>=1 and n<=100:
	for i in range(n):
		t=[(x) for x in input().split()]
		assert len(t)==1
		lst.append(t)
for i in lst:
	y=i[0]
	if len(y)>=1 and len(y)<=100:
		c=y.lower()
		z.append(c)
for i in z:
		if len(i)>10:
			pos1=i[0]
			l=len(i)
			pos2=i[l-1]
			l=l-2
			l=str(l)
			print(pos1+l+pos2)
		else:
			print(i)
		
		
	
	
	