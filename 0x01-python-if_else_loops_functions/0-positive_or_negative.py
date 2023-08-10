#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{} is {}".format(number, "negative" if number < 0 else "positive"))
