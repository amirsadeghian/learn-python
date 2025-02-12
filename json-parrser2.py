import json
import urllib.request, urllib.parse

params = dict()
params[''] = "Michigan State University"
url ='http://py4e-data.dr-chuck.net/opengeo?q='+ urllib.parse.urlencode(params)
uh = urllib.request.urlopen(url)
data = uh.read()

dt = json.loads(data)

print(dt['features'][0]['properties']['plus_code'])