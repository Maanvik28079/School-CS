def makeListStr(ls):
    while True: 
        var = input("Enter Element of list 1: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(var)

    return ls

l1 = []
l1 = makeListStr(l1)
dict_final = {}

for l in l1:
    if l in dict_final:
        dict_final[l] = dict_final.get(l) + 1
    else:
        dict_final[l] = 1

print(dict_final)