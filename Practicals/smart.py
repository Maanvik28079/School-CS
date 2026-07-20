from tabulate import tabulate


data = []
for a in range(1, 7):
    b = 5.5
    while b < 13:
        tempdata = []
        i = 2*a + b
        tempdata.append(a)
        tempdata.append(b)
        tempdata.append(i)
        data.append(tempdata)
        b += 0.5
        
        
    
headers = ["Val_y", "Val_x", "Val_i"]

# Generate a grid-style table
print(tabulate(data, headers=headers, tablefmt="grid"))
