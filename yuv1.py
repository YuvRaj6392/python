n=int(input())
lst=list()
lst1=list()
lst2=list()
lst3=list()
for i in range(n):
	lst=[]
	lst1=[]
	lst2=[]
	lst3=[]
	t=input()
	t=t.split()
	lst.append(t)
	s=input()
	s=s.split()
	lst2.append(s)
	for i in range(0,len(lst)):
		for y in range(0,len(lst[i])):
			k=int(lst[i][y])
			lst1.append(k)
	for i in range(0,len(lst2)):
		for y in range(0,len(lst2[i])):
			d=int(lst2[i][y])
			lst3.append(d)
	m=sum(lst3)//lst1[1]
	if m<lst1[2]:
		print(m)
	else:
		print(lst1[2])
		

		
	
	

