t=int(input())
if t%2!=0 or t<=2:
	print("NO")
else:
	for i in range(2,t+1,2):
		s=t-i
		if s%2==0:
			print("YES")
			break
	for i in range(2,t+1,2):
		s=t-i
		if s%2!=0:
			print("NO")
