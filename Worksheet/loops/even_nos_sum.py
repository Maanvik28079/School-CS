n = int(input("Enter number: "))
ind = 0
sum = 0
no = 1

while True:
    if ind != n:
        if no % 2 == 0:
            ind += 1
            sum += no

        no += 1

    else:
        break

print(sum)