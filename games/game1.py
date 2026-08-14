from random import randint as rd
import csv

range_ = int(input("Enter range of numbers: "))

n = rd(0, range_)
counter = 0

while True:
    try:
        guess = int(input("Enter your gues: ").strip())
    except Exception as e:
        continue
    
    if guess > n:
        counter += 1
        print("Go Lower!")
        
    elif guess < n :
        counter +=1
        print("Go higher! ")
        
    else:
        print(f"Perfect! It only took you {counter + 1} tries :) ")
        break