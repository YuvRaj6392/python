lst=[5,3,8,6,7,2]
for i in range(5):
	min=i
	for y in range(i,6):
		if lst[y]<lst[min]:
			min=y
	lst[i],lst[min]=lst[min],lst[i]
	print(lst)

		