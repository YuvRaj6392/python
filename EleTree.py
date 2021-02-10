import xml.etree.ElementTree as ET
data='''<stuff>
<users>
<user x="1">
<name>yuvraj</name>
<id>1001</id>
</user>
<user x="2">
<name>amir</name>
<id>1002</id>
</user>
</users>
</stuff>'''
stuff=ET.fromstring(data)
lst=stuff.findall("users/user")
for i in lst:
	print('name:',i.find('name').text)
	print('id:',i.find('id').text)
	print('Attribute:',i.get('x'))

