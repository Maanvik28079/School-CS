num = int(input("Enter the number: "))
num_save = num
ls = []
while num != 0:
    ls.append(str(num % 10))
    num = num // 10
    
if int("".join(ls)) == num_save:
    print(f"{num_save} is a palindrome")
    
else:
    print(f"{num_save} is not a palindrome")