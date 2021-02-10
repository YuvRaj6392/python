n=int(input())
k=0
for i in range(n):
	t=input()
	if t[0]=="+" or t[1]=="+":
		k=k+1
	else:
		k=k-1
print(k)
	