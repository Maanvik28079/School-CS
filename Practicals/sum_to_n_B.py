n = int(input("What is the value of n? "))
sum = 0
for i in range(1, n+1):
    sum += i/((i+1) ** (1/2))
    
print(sum)