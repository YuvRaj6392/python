a=[int(x) for x in input().split()]
assert len(a)==2
n=a[0]
k=a[1]
p=k-1
c=0
s=0
b=[int(x) for x in input().split()]
assert len(b)==n
l=len(b)
for i in range(k,l):
	if b[p]==0:
		print(c)
		quit()
	elif b[p]<=b[i] and b[i]!=0:
		s=s+1
print(s+k)

		

		





