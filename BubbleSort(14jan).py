lst=list()
while True:
	n=input()
	if n=="done":
		break
	else:
		try:
			n=int(n)
			lst.append(n)
		except:
			print("not a number")
print("Unsorted list",lst)
for i in range(len(lst)-1,0,-1):
	for y in range(i):
		if lst[y]>lst[y+1]:
			lst[y],lst[y+1]=lst[y+1],lst[y]
print("After bubble sort",lst)