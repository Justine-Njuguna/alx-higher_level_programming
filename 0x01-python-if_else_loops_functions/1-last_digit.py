#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lsd = str(number)[-1]

print(f"Last digit of {number} is {lsd}", end=" ")

if lsd > "5":
    print("and is greater than 5")
elif lsd == "0":
    print("and is 0")
else:
    print("and is less than 6 and not 0")
