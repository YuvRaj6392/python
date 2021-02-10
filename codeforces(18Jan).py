a=[int(x) for x in input().split()]
l=a[0]
b=a[1]
c=0
while True:
	l=l*3
	b=b*2
	c=c+1
	if l>b:
		break
print(c)