#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = 0
if number < 0:
    number *= -1
    no = 1
lastdigit = number % 10
if no == 1:
    number *= -1
    lastdigit *= -1
print("Last digit of {:d} is ".format(number), end="")
if lastdigit > 5:
    print("{:d} and is greater than 5".format(lastdigit))
elif lastdigit == 0:
    print("{:d} and is 0".format(lastdigit))
else:
    print("{:d} and is less than 6 and not 0".format(lastdigit))
