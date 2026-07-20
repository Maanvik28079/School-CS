s1 = int(input("Length of the first side (in cms): "))
s2 = int(input("Length of the second side (in cms): "))
s3 = int(input("Length of the third side (in cms): "))

if s1==s2==s3:
    print("Equilateral Triangle")
elif s1==s2 or s2==s3 or s1==s3:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")