l1 = []
l1.append(int(input("Enter the first number: ")))
l1.append(int(input("Enter the second number: ")))
l1.append(int(input("Enter the third number: ")))

l1.sort()

print(f"Highest number is {l1[-1]}")
print(f"Middle number is {l1[1]}")
print(f"Smallest number is {l1[0]}")