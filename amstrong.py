num = int(input("Enter the number: "))
num_save = num
amstrong_sum = 0
while num != 0:
    amstrong_sum += (num % 10) ** (len(str(num_save)))
    print(amstrong_sum)
    num = num // 10

if amstrong_sum == num_save:
    print(f"{num_save} is an Armstrong number")

else:
    print(f"{num_save} is not an Armstrong number")