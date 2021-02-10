t=int(input())
for i in range(t):
	a=[]
	a=[int(x) for x in input().split()]
	n=a[0]
	k=a[1]
	j=1
	lst=[]
	for i in range(n):
		lst.append(j)
	t=0
	while True:
			if sum(lst)%k==0:
				for i in range(1,len(lst)):
					t=t+lst[i]
				if n==k:
					print("1")
					break
				elif t==lst[0]:
					print(sum(lst)//k)
					break
				else:
					print(abs(lst[0]-t))
					break
			else:
				j=j+1
				lst[0]=j
				
				
			
		
		

		
