largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        else:
            num = float(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        

print("Maximum is", int(largest))
print("Minimum is", int(smallest))