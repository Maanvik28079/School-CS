number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Enter operator: ")

if operation == "+":
    print(f"{number1}+{number2} = {number1+number2}")
elif operation == "-":
    print(f"{number1}-{number2} = {number1-number2}")
elif operation == "*":
    print(f"{number1}*{number2} = {number1*number2}")
elif operation == "/":
    print(f"{number1}/{number2} = {number1/number2}")
