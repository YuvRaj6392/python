a=[int(x) for x in input().split()]
n=a[0]
k=a[1]
s=0
for i in range(0,k):
	s=n%10
	if s==0:
		n=n//10
	else:
		n=n-1
print(n)