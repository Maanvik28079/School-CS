n = int(input(""))
for i in range(2, 5):
    num = n*i
    print(num)
    if num % 4 == 0:
        print("Multiple of four")