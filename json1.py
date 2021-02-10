import urllib.request,urllib.error,urllib.parse
import json
api_key=42
service_url='http://py4e-data.dr-chuck.net/json?'
parms=dict()
address=input("Enter the address:")
parms['address']=address
parms['key']=api_key
url=service_url+urllib.parse.urlencode(parms)
uh=urllib.request.urlopen(url).read()
data=uh.decode()
js=json.loads(data)
print(json.dumps(js,indent=4))
plus=js['results'][0]['geometry']['location']['lat']
minus=js['results'][0]['geometry']['location']['lng']
print(plus)
print(minus)
