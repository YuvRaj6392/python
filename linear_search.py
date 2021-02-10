pos=0
def search(list,n):
	for i in range(0,len(list)):
		if list[i]==n:
			globals()['pos']=i
			return True
list=[45,22,11,78,99]
n=99
if search(list,n):
	print("Found at index",pos)
else:
	print("Not found")