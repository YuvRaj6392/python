lst=list()
lst1=list()
t=int(input())
m=1
for i in range(t):
	n=int(input())
	lst.append(n)
for i in range(2):
	maxi=max(lst)
	lst1.append(maxi)
	lst.remove(maxi)
for i in lst1:
	m=m*i
print(m)
	
