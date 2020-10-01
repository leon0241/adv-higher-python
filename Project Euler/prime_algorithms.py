import math

def find_primes(n):
    primeList = []
    for i in range(1, n, 2):
        primeList.append(i)

    for i in range(3, (int(math.sqrt(n)) + 1), 2):
        #cycle for i = 3
        for j in primeList:
            if j % i == 0 and j > i:
                primeList.remove(j)
    return primeList

def find_max_prime(n):
    list = find_primes(n)
    return max(list)

def check_prime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    print("not done yet :D")
