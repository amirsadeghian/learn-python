import urllib.request
req = urllib.request.Request('https://sadeghian.us', headers={'User-Agent' : "Magic Browser"}) 
res = urllib.request.urlopen( req )
for line in res:
    print(line.decode().strip())