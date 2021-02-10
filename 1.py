from numpy import *
c=0
s=0
r=0
m=0
g=0
arr1=([1,2,3],[1,2,3])
for i in range(0,len(arr1)):
		s=arr1[i][2]
		q=s//2
		r=s%2
		c=c+q
		m=m+r
g=m//2
c=c+g
print(c)
		