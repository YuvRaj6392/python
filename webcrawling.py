import urllib.request, urllib.parse, urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
fname=input("Enter the url properly:")
fh=urllib.request.urlopen(fname,context=ctx)
for i in fh:
	i=i.decode().rstrip()
	print(i)
