inp = input("Enter a number")
try:
    inp = int(inp)
    print("Number is",inp)
except:
    print("Error! Input wasn't a number")