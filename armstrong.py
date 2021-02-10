for i in range(1,1001):
	if i<100:
		t=i
		s=0
		while t>0:
			d=t%10
			c=d*d
			s=s+c
			t=int(t/10)
		if s==i:
			print(s)
	elif i>100 and i<=1000:
		t=i
		s=0
		while t>0:
			d=t%10
			c=d*d*d
			s=s+c
			t=int(t/10)
		if s==i:
			print(s)
			
		