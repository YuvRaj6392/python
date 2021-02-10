a=[int(x) for x in input().split()]
m=a[0]
n=a[1]
x=c=t=l=t=g=0
for i in range(n):
	x=m//2
	c=c+x
	t=m-(2*x)
	l=l+t
g=l//2
print(c+g)