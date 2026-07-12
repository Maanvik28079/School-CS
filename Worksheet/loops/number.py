num = int(input("Enter the number: "))
print(len(str(num)))
sum = 0
for n in str(num):
    sum += int(n)

print(sum)