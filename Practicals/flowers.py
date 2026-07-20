flowers_dict = {}

def makeListStr(ls, flower):
    while True: 
        var = input(f"Enter a colour in which {flower}s are found: (enter e to end) ")

        if var.lower() == "e":
            break

        else:
            ls.append(var)

    return ls


while True:
    flower = input("Enter flower name (press e to end): ")
    
    if flower.lower().strip() == 'e':
        break
    
    l1 = []
    l1 = makeListStr(l1, flower)
    
    flowers_dict[flower] = tuple(l1)


max_len = 0
flower_max = ""
for f in flowers_dict:
    if len(flowers_dict[f]) > max_len:
        max_len = len(flowers_dict[f])
        flower_max = f
        
        
values = flowers_dict.values()
all_colours = {}
for value in values:
    for tup in value:
        if tup in all_colours:
            all_colours[tup] = all_colours[tup] + 1
        else:
            all_colours[tup] = 1
        
print(f"The flower which exists in the most colours is: {flower_max}")

max_flowers = max(all_colours.values())
max_colours_ls = []

for key, value in all_colours.items():
    if all_colours[key] == max_flowers:
        max_colours_ls.append(key)

print(f"The colour(s) in which the most flowers exist is/are: {", ".join(max_colours_ls)}")