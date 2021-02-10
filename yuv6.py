f=1
lst1=list()
n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)
for i in range(2):
	maxi=max(a)
	lst1.append(maxi)
	a.remove(maxi)
for i in lst1:
	f=f*i
print(f)