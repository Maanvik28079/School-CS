while(1):
    num = int(input("Enter num"))
    if num % 3 == 0:
        print(num)
    elif num % 4 == 0:
        print(num - 2)
        pass
    else:
        print(num + 3)