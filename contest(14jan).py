t=int(input())
for i in range(t):
	a=input()
	b=input()
	if len(a)>len(b) and len(a)%len(b)!=0:
			print("-1")
	elif len(a)>len(b):
			t=len(b)
			for i in range(t):
				print(b,end="")
			print()
	elif len(b)>len(a):
		t=len(b)
		for i in range(t):
			print(a,end="")
		print()