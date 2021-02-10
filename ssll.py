import urllib.request,urllib.parse,urllib.error
import re
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
lst=list()
s=0
url=input("Enter the url:")
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
	a=tag.get('href',None)
	y=tag.contents[0]
	print(a)
	print(y)
	print()