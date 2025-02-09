import json
import urllib.request

url ='http://py4e-data.dr-chuck.net/comments_2173662.json'
uh = urllib.request.urlopen(url)
data = uh.read()

dt = json.loads(data)
comments = dt['comments']
sum = 0
for i in comments:
    sum+= int(i['count'])
print(sum)