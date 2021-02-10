fname = input("Enter file:")
fh=open(fname)
count=dict()
for i in fh:
	i=i.rstrip()
	if i.startswith("From"):
		word=i.split()
		t=word[1]
		if t in count:
			count[t]=count[t]+1
		else:
			count[t]=1
	else:
		continue
bigcount=None
bigword=None
for k,v in count.items():
	if bigcount is None or v>bigcount:
		bigword=k
		bigcount=v
bigcount=bigcount-5
print(bigword,bigcount)
