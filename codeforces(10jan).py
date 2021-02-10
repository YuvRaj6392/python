i=0
a=[int(x) for x in input().split()]
n=a[0]
s=a[1]
h=0
while s>0:
	x=n//2
	i=n-(2*x)
	h=h+1
	s=s-1
if h//2!=1:
	h=h+1
	print(h)
	quit()
else:
	print(h)
	quit()