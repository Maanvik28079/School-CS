import string

upper_ls = list(string.ascii_uppercase)

n = int(input("What is the range? "))

for i in range(n, 0, -1):
    for j in range(0, i):
        print(upper_ls[j], end="    ")
    print("")

