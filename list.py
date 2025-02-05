friends = ["jo","Glenn","Sally"]

print(len(friends))
for friend in friends:
    print(friend)

friends.sort()
print(friends)


stuff = list()
stuff.append("Book")
stuff.append("Pen")
print(stuff)
if "Apple" not in stuff:
    print("Didn't find apple")


abc = "White;three;words"
stuff = abc.split(";")
print(stuff[1])