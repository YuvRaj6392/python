lst=[4,7,99,45,8,12]
lst.sort()
l=mid=0
u=len(lst)-1
n=int(input("Enter the number to find from the list: "))
while l<=u:
	mid=(l+u)//2
	if lst[mid]==n:
		print("Found at index position",mid)
		quit()
	else:
		if lst[mid]<n:
			l=mid+1
		else:
			u=mid-1
print("Not Found")
	