import re

linex = "Hello I am From Miami"
if(re.search('^Hello',linex)):
    print("Found")

x = "My 3 favorite numbers are 9 and 23"
res = re.findall('[0-9]+',x)
print(res)