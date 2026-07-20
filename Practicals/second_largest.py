def makeList(ls):
    while True: 
        var = input("Enter Element of list 1: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(int(var))

    return ls

l1 = []
l1 = makeList(l1)
l1.pop(l1.index((max(l1))))
print(f"Second largest number is: {max(l1)}")