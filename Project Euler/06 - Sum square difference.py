#The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

value = 100

def find_sum(n):
    sum = 0
    sumsq = 0
    for i in range(1, n + 1):
        sumsq += i**2
        sum += i
    return sum, sumsq

def find_square_of_sum(n):
    return n**2

def main():
    a, b = find_sum(value)
    c = find_square_of_sum(a)
    difference = c - b
    print(difference)

main()
