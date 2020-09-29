import math

value = 600851475143

def find_primes(val):
    primeList = []
    for i in range(1, val, 2):
        primeList.append(i)
    print(primeList)

    for i in range(3, (int(math.sqrt(val)) + 1), 2):
        #cycle for i = 3
        for j in primeList:
            if j % i == 0 and j > i:
                primeList.remove(j)
    return primeList

print(value)
print(find_primes(value))
