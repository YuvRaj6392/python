t=int(input())
lst=list()
for i in range(t):
	a=[int(x) for x in input().split()]
	lst.append(a[0])
	lst.append(a[1])
sum=max=0
for i in range(1,len(lst)+1):
		if i%2!=0:
			sum=sum-lst[i-1]
		else:
			sum=sum+lst[i-1]
			if sum>max or max==0:
				max=sum
print(max)

		
		