lst=list()
lst1=list()
t=input()
t=t.split()
lst.append(t)
for i in range(0,len(lst)):
	for y in range(0,len(lst[i])):
		k=float(lst[i][y])
		lst1.append(k)
if lst1[0]%5==0 and lst1[0]<lst1[1]:
	k=lst1[1]-lst1[0]-0.50
	k="{:.2f}".format(k)
	print(k)
elif lst1[0]%5!=0:
	z=lst1[1]
	z="{:.2f}".format(z)
	print(z)
else:
	a=lst1[1]
	a="{:.2f}".format(a)
	print(a)
	
