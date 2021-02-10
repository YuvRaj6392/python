a=[int(x) for x in input().split()]
x1=a[0]
y1=a[1]
b=[int(x) for x in input().split()]
x2=b[0]
y2=b[1]
m=abs(y1-y2)
n=abs(x1-x2)
print(max(m,n))