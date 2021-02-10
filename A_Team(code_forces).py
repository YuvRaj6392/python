n=int(input())
lst=list()
lst1=list()
m=0
for i in range(n):
	t=input()
	words=t.split()
	lst.append(words)
for i in range(0,len(lst)):
				c=0
				for y in range(0,len(lst[i])):
					t=int(lst[i][y])
					if t==1:
						c=c+1
				if c>=2:
					m=m+1
print(m)
				
				
				
		
		
	