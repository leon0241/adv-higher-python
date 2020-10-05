#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
import prime_algorithms as palgs

value = 600851475143
primeList = []
primeFactors = []

def find_factor(value, list): #Finds the prime factor
    maxVal = 0 #Max value = 0
    for i in range(1, int(math.sqrt(value))): #From 1 to rounded square root of value. just use sqrt when finding prime numbers lol
        if value % i == 0: #Checks if i is a factor
            check = False #Resets check
            check = palgs.check_prime(i) #Checks if i is a prime
            if check == True and maxVal < i: #Checks if i is a larger prime factor
                maxVal = i #Sets to largest prime factor if so
    return maxVal

print(find_factor(value, primeList))
#primeFactors = find_prime_factors(value, primeList)
#print(primeFactors)
