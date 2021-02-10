import timeit

start = timeit.default_timer()
a=0
b=1
n=int(input("Enter the number:"))
if n<=1:
	print(a)
else:
	print(a)
	print(b)
	while(n-2>0):
		c=a+b
		a=b
		b=c
		n=n-1
print(c)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in "+str(execution_time))