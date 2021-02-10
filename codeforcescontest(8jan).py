t=int(input())
for i in range(t):
	n=int(input())
	lst1=[int(x) for x in input().split()]
	assert len(lst1)==n
	l=len(lst1)
	m=l-2
	c=0
	s=0
	a=1
	y=1
	for i in range(m):
					if lst1[a]<lst1[a+y]:
						c=c+1
						y=y+1
					elif lst1[a]>lst1[a+y]:
						s=s+1
						y=y+1
	if c<s:
						print(c)
	elif s<c:
						print(s)
	else:
						print(c)
						
						
						
						
					
				
				
	
	