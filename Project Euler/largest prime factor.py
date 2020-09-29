#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

value = 600851475143
primeList = []
primeFactors = []

def find_factors(value, list):
    for i in range(1, value):
        if value % i == 0:
            list.append(i)
    return list

def find_primes(val):
    primeList = []
    for i in range(1, val, 2):
        primeList.append(i)

    for i in range(3, (sqrt(val) + 1), 2):
        #cycle for i = 3
        for j in primeList:
            if primeList[j] % i = 0:
                primeList.remove(j)
    return primeList


primeList = find_factors(value, primeList)
#primeFactors = find_prime_factors(value, primeList)
print(primeList)
#print(primeFactors)
