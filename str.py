mystr = "Hello World!"
if("H" in mystr):
    print("Found")

result = mystr.find('W');
if(result!=-1):
    print("Found W!")

newstr = mystr.replace('Hello','Bye')
print(newstr)