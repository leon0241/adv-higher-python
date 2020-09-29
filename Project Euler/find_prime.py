val = 6857

def find_prime(n):
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

print(find_prime(val))
