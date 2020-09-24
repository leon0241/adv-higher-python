#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

value = 13195
primeList = []
primeFactors = []

for i in range(1, value):
    if value % i == 0:
        primeList.append(i)
for j in primeList:
    factors = 0
    for k in range(1, primeList[j]):
        if j % k == 0:
            factors += 1
    if factors <= 2:
        primeFactors.append(primeList[j])

print(primeList)
print(primeFactors)
