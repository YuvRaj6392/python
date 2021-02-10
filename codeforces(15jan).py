n=input()
lst=list()
count=dict()
for i in range(len(n)):
	lst.append(n[i])
for i in lst:
	if i not in count:
		count[i]=1
	else:
		count[i]=count[i]+1
if (len(count.values()))%2==0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")