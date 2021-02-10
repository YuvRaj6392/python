import urllib.request,urllib.parse,urllib.error
fname=input("Enter url:")
fh=urllib.request.urlopen(fname)
for i in fh:
	i=i.decode().rstrip()
	print(i)
