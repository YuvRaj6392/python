s=input()
t=len(s)
lst=list()
for i in range(0,t,2):
	lst.append(s[i])
lst.sort()
for i in range(1,t-1,2):
	lst.insert(i,"+")
for i in lst:
	print(i,end="")

