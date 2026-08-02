def checkprime(num):

    if num == 1:
        return False
    for i in range(2, int((num ** 0.5) + 1)):
        if num % i == 0:
            return False
    return True


for i in range(11):
    a, b = input("Enter comma seperated pairs ").strip().split(",")
    a, b = int(a.strip()), int(b.strip())

    if abs(a-b) != 2:
        continue

    else:
        if checkprime(a) and checkprime(b):
            print("Twin primes")

