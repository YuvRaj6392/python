lst=list()
lst1=list()
t=input().split()
lst.append(t)
for i in range(len(lst)):
	for y in range(len(lst[i])):
		k=int(lst[i][y])
		lst1.append(k)
print(sum(lst1))