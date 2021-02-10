import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url="http://py4e-data.dr-chuck.net/known_by_Suzi.html"
for i in range(7):
	html=urllib.request.urlopen(url).read()
	soup=BeautifulSoup(html,'html.parser')
	tags=soup('a')
	count=0
	for tag in tags:
		count=count+1
		if count>18:
			break
		url=tag.get('href',None)
print(url)