bill = float(input("Enter bill amount: "))
print("")

if bill >= 15000:
    print(f"Final bill is ${0.75*bill}")

elif bill >= 10000:
    print(f"Final bill is ${0.85*bill}")

elif bill >= 8000:
    print(f"Final bill is ${0.90*bill}")

elif bill >= 6000:
    print(f"Final bill is ${0.95*bill}")

elif bill >= 4000:
    print("You get a free coupon for 10% discount on your next order !!")
    print(f"Your final bill is ${bill}")

elif bill >= 2000:
    print(f"You get a free coupon for 5% discount on your next order !!")
    print(f"Your final bill is ${bill}")
    

    
print("")