#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else:
    digit = ((number * -1) % 10) * -1

message = "digit of %d is %d and is" % (number, digit)

if digit == 0:
    print(message, "0")
elif digit > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")
