x = int(input("What is the value of x ? "))
n = int(input("What is the value of n ? "))
sum = 0
for i in range(1, n+1):
    sum +=  (x**i)/x
    
print(sum)