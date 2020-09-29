import math
def find_primes(val):
    primeList = []
    for i in range(1, val, 2):
        primeList.append(i)
    print(primeList)

    for i in range(3, (int(math.sqrt(val)) + 1), 2):
        #cycle for i = 3
        for j in primeList:
            print(j)
            if j % i == 0:
                primeList.remove(j)
                print(primeList)

    return primeList

print(find_primes(70))
