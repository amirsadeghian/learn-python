myfile = open("text.txt")
for line in myfile:
    if(line.startswith('Get')):
        print(line.rstrip())
myfile.close()

myfile2 = open("text.txt")
buf = myfile2.read()
print(buf)

filename = input("Enter the file name:")
try:
    fh = open(filename)
except:
    print("File doesn't exist!")
    quit()
count = 0
for line in fh:
    print(line.rstrip())
    count+=1
print("There were",count,"lines in the file.")