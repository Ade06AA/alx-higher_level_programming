#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
an = abs(number)
if an % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif an % 10 > 5:
    print(f"Last digit of {number} is {an % 10} and is greater than 5")
else:
    print(f"Last digit of {number} is {an % 10} and is less than 6 and not 0")
