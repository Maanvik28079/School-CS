a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
n = int(input("Enter range: "))
sum = 0
for i in range(1, n+1):
    sum += (i*a + b)
print(sum)