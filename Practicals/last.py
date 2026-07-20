ls = list(input("What is the number "))

if int(ls[-2]) %2 == 0:
    print("The second last digit is even")
else:
    print("The second last digit is odd")

if int(ls[-1]) %2 == 0:
    print("The last digit is even")
else:
    print("The last digit is odd")
