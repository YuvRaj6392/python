import urllib.request, urllib.parse, urllib.error
from py4e import BeautifulSoup
url=input("Enter url")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
for tag in tags:
	print(tag.get('href'),None)