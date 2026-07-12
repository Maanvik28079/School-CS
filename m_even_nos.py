sum = int(input("Waht is the value of M: "))
summm = 0
for i in range(1, 2*sum+1):
    if i %2 == 0:
        summm += i

print(summm)