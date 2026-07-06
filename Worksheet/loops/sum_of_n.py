sum = int(input("Enter a number(or q to stop): "))

while True:
    n = input("No: ")

    if n != "q":
        sum += int(n)
    else:
        break

print(sum)