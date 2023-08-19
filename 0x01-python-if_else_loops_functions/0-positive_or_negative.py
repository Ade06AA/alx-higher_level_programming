#!/usr/bin/python3
import random
number = random.randint(-10, 10)
num = number
print("{} is {}".format(num, "negative" if num < 0 else
                        "positive" if num != 0 else "zero"))
