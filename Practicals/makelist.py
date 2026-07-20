def makeList(ls):
    while True: 
        var = input("Enter Element of list 1: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(int(var))

    return ls

def makeListStr(ls):
    while True: 
        var = input("Enter Element of list 1: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(var)

    return ls