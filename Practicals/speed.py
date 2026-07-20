from datetime import date
speed = int(input("Speed of car: "))


def is_bday(bday):
    today = date.today()
    bday_month = int(bday[5:7])
    bday_day = int(bday[8:10])
    
    return today.month == bday_month and today.day == bday_day

# Example usage
if (is_bday(input("Whats your birthday?[yyyy-mm-dd]: "))):
    speed == speed
else:
    speed += 5
    

if speed <= 60:
    print("0")
elif speed <= 80:
    print("1")
else:
    print('2')