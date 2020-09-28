#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

value = 600851475143
primeList = []
primeFactors = []

def find_factors(value, list):
    for i in range(1, value):
        if value % i == 0:
            list.append(i)
    return list

def find_prime_factors(value, list):
    primeFactorsList = []
    for i in range(len(list)):
        factors = 0
        for j in range(1, list[i]):
            if list[i] % j == 0:
                factors += 1
        if factors <= 2:
            primeFactorsList.append(list[i])
    return primeFactorsList


primeList = find_factors(value, primeList)
primeFactors = find_prime_factors(value, primeList)
print(primeList)
print(primeFactors)
