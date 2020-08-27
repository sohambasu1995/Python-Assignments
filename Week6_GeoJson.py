"""
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
"""
import json,ssl
import urllib.request,urllib.parse, urllib.error



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key=42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

address = input("Enter your desired address:")
parameters = {'address':address, 'key':api_key}
data=urllib.parse.urlencode(parameters)

url=serviceurl.strip() + data.strip()
handle=urllib.request.urlopen(url, context=ctx).read().decode()

js=json.loads(handle)

#not required. just to check
#print(json.dumps(js,indent = 4))

place_id = js["results"][0]["place_id"]
print("Place Id is",place_id)
