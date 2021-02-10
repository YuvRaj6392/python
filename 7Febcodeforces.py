t=int(input())
for i in range(t):
	a=input()
	lst=[]
	for i in range(0,len(a),2):
		t=ord('a')
		if a[i]=='a':
			t=t+1
			lst.insert(i,chr(t))
		else:
			t=ord(a[i])
			t=t-1
			lst.insert(i,chr(t))
	for i in range(1,len(a),2):
		t=ord('z')
		if a[i]=='z':
			t=t-1
			lst.insert(i,chr(t))
		else:
			lst.insert(i,chr(t))
	for i in lst:
			print(i,end="")
	print()
			
		