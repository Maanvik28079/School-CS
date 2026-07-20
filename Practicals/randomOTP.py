from random import randint as rint
ls = []

while True:
    i = str(rint(0, 9))
    if i not in ls:
        ls.append(i)

        if len(ls) == 6:
            break

print("".join(ls))