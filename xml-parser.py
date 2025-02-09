import urllib.request
import xml.etree.ElementTree as ET

url ='http://py4e-data.dr-chuck.net/comments_2173661.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
for result in counts:
    sum+=int(result.text)
print(sum)