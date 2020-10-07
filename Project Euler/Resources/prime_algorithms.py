import math

def find_primes(n): #Finds primes below n
    primeList = [2]
    for i in range(3, n, 2):
        primeList.append(i) #Makes array of odd number to number n(even numbers are not prime)

    for i in range(3, (int(math.sqrt(n)) + 1), 2):
        #cycle for i = 3
        for j in primeList:
            if j % i == 0 and j > i:
                primeList.remove(j)
    return primeList

def find_max_prime(n): #Finds the largest prime below n
    list = find_primes(n)
    return max(list)

def check_prime(n): #Checks if n is a prime
    if n == 1: #Checks if n = 1
        return False #Is not prime
    elif n <= 3: #Checks if n = 2 or 3
        return True #Is prime

    i = 5
    while i * i <= n: #k±1 shows prime number idk
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True #Returns true if it is prime

def find_nth_prime(n): #Finds nth prime
    #Inequality for nth prime
    #pn > n*ln(n*ln(n)) for n ≥ 6.
    upperBound = n * math.log(n * math.log(n)) #Sets upper boundary
    intUpper = round(upperBound) #Rounds to nearest integer
    primeList = find_primes(intUpper) #Finds of primes below boundary
    return primeList[n - 1] #Return nth prime
