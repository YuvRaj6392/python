n=int(input())
a=input()
r=b=g=0
for i in range(1,n):
	if a[i-1]==a[i]:
		if a[i]=="R":
			r=r+1
		elif a[i]=="B":
			b=b+1
		else:
			g=g+1
print(r+b+g)