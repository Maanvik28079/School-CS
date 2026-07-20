list1 = []
list2 = []

def makeList(ls):
    while True: 
        var = input("Enter Element of list 1: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(int(var))

    return ls

def eveAndodd(ls):
    f_list = []
    for i in range(0, len(ls)):
        try:
            if ls[i] % 2 == 0:
                if ls[i + 1] % 2 != 0:
                    f_list.append(ls[i])
        except IndexError:
            return f_list

    return f_list

list1 = makeList(list1)
lsit2 = makeList(list2)

set_common = set(list1) & set(list2)

print(f"All common elements: {list(set_common)}")

print(f"Elements of List 1 satisfying the condition: {eveAndodd(list1)}")
print(f"Elements of List 2 satisfying the condition: {eveAndodd(list2)}")
exit()