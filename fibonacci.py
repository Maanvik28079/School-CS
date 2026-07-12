def fibonacci(num):
    if num == 2:
        return 1

    elif num == 1:
        return 0
    else:
        return fibonacci(num - 1) + fibonacci(num - 2) 

print(fibonacci(int(input("Enter the number: "))))