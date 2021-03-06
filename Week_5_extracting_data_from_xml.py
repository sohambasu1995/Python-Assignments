"""
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file
"""

import urllib.error, urllib.request, urllib.parse
import re, ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input("Enter URL: ")
uh = urllib.request.urlopen(inp).read()

tree=ET.fromstring(uh)
lst=tree.findall('comments/comment')
lst1=list()

for i in lst:
    a=int(i.find('count').text)
    lst1.append(a)
print("Count:",len(lst))
print("Sum:",sum(lst1))
