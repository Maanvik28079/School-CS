choice = int(input("Choose pattern(1 or 2): "))
h = int(input("Height of tower: "))
i = 1

if choice == 1:
    for i in range(h+1):
        print("*"*i)
        
elif choice == 2:
    for i in range(h+1):
        print(" "*(5-i) + "*"*i)