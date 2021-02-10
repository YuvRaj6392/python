t=int(input())
for i in range(0,t):
	lst=[]
	lst1=[]
	lst2=[]
	n=int(input())
	a=[int(x) for x in input().split()]
	lst.append(a)
	s=0

	for i in range(0,len(lst)):
		for y in range(0,len(lst[i])):
			lst1.append(lst[i][y])
	lst[-1]=1
	for i in range(-1,len(lst1)-1):
			if lst1[i]>=lst1[i+1]:
				s=s+1
				
				lst2.append(s)
			else:
				s=s-1
				
				lst2.append(s)
	print(max(lst2))
	
			
	
		
		