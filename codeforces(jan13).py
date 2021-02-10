m=n=0
lst=list()
for i in range(5):
	a=[int(x) for x in input().split()]
	lst.append(a)
for i in range(0,len(lst)):
	for y in range(0,len(lst[i])):
		if lst[i][y]==1:
			m=i-2
			n=y-2
			print(abs(m)+abs(n))
			quit()
	


