n = int(input("Number of students is: "))
GrpA = 0
GrpB = 0
GrpC = 0
GrpD = 0

for i in range(1, n+1):
    age = int(input("What is the students age?: "))
    if age < 12:
        GrpD += 1
    elif age < 15:
        GrpA += 1
    elif age < 17:
        GrpB += 1
    elif age < 19:
        GrpC += 1
        
        
print(f"Group A: 12 yrs and above but less than 15 yrs   - {GrpA}")
print(f"Group A: 15 yrs and above but less than 17 yrs   - {GrpB}")
print(f"Group A: 17 yrs and above but less than 19 yrs   - {GrpC}")
print(f"Group DL Lesser than 12 yrs                      - {GrpD}")