ls = []
while True:

    num = input("Enter a number (press q to quit): ")
    if num != "q":
        ls.append(int(num))
    else:
        break

print(sorted(ls)[-2])