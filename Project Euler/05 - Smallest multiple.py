# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import functools

numberRange = 20 #Range of number

def numbers(): #creates array from 1 to 20
    arr = []
    for i in range(1, (numberRange + 1)):
        arr.append(i)
    return arr

def find_lcm(x, y): #Finds lowest common multiple (Using the greatest common divisor)
    z = find_gcd(x, y)
    val = (x / z) * y
    return val

def find_gcd(x, y): #Finds greatest common divider (Euclid's algorithm)
    while y != 0:
        t = y
        y = x % y
        x = t
    return x

numbers = numbers()
lcm = functools.reduce(find_lcm, numbers)
print(lcm)
