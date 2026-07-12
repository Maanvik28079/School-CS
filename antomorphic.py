num = int(input("Enter the numebr: ").strip())

if str(num ** 2).endswith(str(num)[-1]):
    print("Number is automorphic")