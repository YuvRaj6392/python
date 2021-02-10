n=input()
t=len(n)
c=s=0
for i in range(t):
	if ord(n[i])>=97 and ord(n[i])<=122:
		s=s+1
	elif ord(n[i])>=65 and ord(n[i])<=90:
		c=c+1
if s>c or s==c:
	print(n.lower())
elif c>s:
	print(n.upper())

	