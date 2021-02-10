lst=list()
lst1=list()
t=input().split()
lst.append(t)
lst2=list()
m=1
for i in range(len(lst)):
	for y in range(len(lst[i])):
		k=int(lst[i][y])
		lst1.append(k)
for i in range(0,2):
	maxi=max(lst1)
	lst2.append(maxi)
	lst1.remove(maxi)
for i in lst2:
	m=m*i
print(m)

	