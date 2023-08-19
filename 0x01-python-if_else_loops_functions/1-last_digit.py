#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
an = abs(number)
s = int((an / number) * (an % 10))
if an % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif s > 5:
    print(f"Last digit of {number} is {s} and is greater than 5")
else:
    print(f"Last digit of {number} is {s} and is less than 6 and not 0")
