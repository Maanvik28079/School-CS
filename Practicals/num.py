n = list(input("What is the number: "))
sum = 0
product = 1
i = 1
for i in range(len(n)):
    if i % 2 == 1:
        product *= int(n[i])
    else:
        sum += int(n[i])
        
print(f"The sum of all odd positioned digit numbers is {sum}")
print(f"The product of all even positioned digits is {product}")
print(f"The sum of the two values mentioned is {sum+product}")