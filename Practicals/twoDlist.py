int1 = int(input("Enter first value: "))
int2 = int(input("Enter second value: "))

ls_final = []

for i in range(0, int1):
    ls_temp = []
    for j in range(0, int2):

        ls_temp.append(i*j)

    ls_final.append(ls_temp)

print(ls_final)