import urllib.request,urllib.parse,urllib.error
import json
uh=open("roster_data.json")
data=uh.read()
js=json.loads(data)
print(json.dumps(js,indent=4))
	