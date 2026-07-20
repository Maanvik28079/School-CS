marks = int(input("How many marks have you achieved? "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A-")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B-")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
elif marks >= 33:
    print("E")
else:
    print("Failed! Needs improvement")