f1=open("IMG1.jpg","rb")
f2=open("IMG2COPY.jpg","wb")
for i in f1:
	f2.write(i)
