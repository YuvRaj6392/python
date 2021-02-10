fname=input("Enter file: ")
fh=open(fname)
count=dict()
lst=list()
for i in fh:
	i=i.rstrip()
	if len(i)<1 or i.startswith("From:"):
		continue
	if i.startswith("From"):
		word=i.split()
		w=word[5]
		y=w[0:2]
		if y in count:
			count[y]=count[y]+1
		else:
			count[y]=1
for k,v in count.items():
	new=(k,v)
	lst.append(new)
lst.sort()
for k,v in lst[:]:
	print(k,v)