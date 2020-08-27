import urllib.request, urllib.error, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp='http://py4e-data.dr-chuck.net/comments_42.json'

url = urllib.request.urlopen(inp).read()
info=json.loads(url)
sum1=0

for item in info['comments']:
    sum1 = sum1 + int(item['count'])
print(sum1)

