import urllib.request,urllib.parse,urllib.error
import json
serviceurl = "http://python-data.dr-chuck.net/geojson?"
while True:
	address=input("Enter your location:")
	url=serviceurl+urllib.parse.				        	urlencode({'address':address})
	uh=urllib.request.urlopen(url)
	data=uh.read().decode()
	js=json.loads(data)
	
	t=js['results'][0]['place_id']
	print('place_id',t)