t=int(input())
count=0
minimum=0
maximum=0
for i in range(t):
	lst=[int(x) for x in input().split()]
	assert len(lst)==2
	n=lst[0]
	m=lst[1]
	a=[int(x) for x in input().split()]
	assert len(a)==n
	b=[int(x) for x in input().split()]
	assert len(b)==m
	while True:
			if sum(a)>sum(b):
				print(count)
				count=0
				break
			else:
					minn=min(a)
					maxx=max(b)
					for i in range(0,len(a)):
						if i==minn:
							minimum=i
					for y in range(0,len(b)):
						if y==maxx:
							maximum=i
					a.remove(minn)
					b.remove(maxx)
					a.insert(minimum,maxx)
					b.insert(maximum,minn)
					count=count+1

	
		
		
		

