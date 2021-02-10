import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET
lst=list()
s=0
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url="http://py4e-data.dr-chuck.net/comments_982748.xml"
html=urllib.request.urlopen(url,context=ctx).read()
tree=ET.fromstring(html)
lst=tree.findall(".//comment")
for i in lst:
	c=i.find('count').text
	f=int(c)
	s=s+f
print(s)

