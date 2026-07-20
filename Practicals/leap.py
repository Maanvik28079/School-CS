year = int(input("What is the year: "))
is_a_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
             is_a_leap_year = True     
    else: 
        is_a_leap_year = True
if is_a_leap_year:
    print("The year is a leap year")
else:
    print("The year is not a leap year")