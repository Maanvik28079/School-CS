ls = []
num = int(input("Enter the number: "))
num_save = num
while num != 0:
    ls.append(str(num % 10))
    num = num // 10

reverse = int("".join(ls)) 

print(f"Reverse of number: {reverse}")

if reverse == num_save:
    print("is a palindrome")
else:
    print("Is not a palindrome")