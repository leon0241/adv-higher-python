#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#<big number>
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def readFile(x):
    f = open(x, "r")
    val = f.readlines()
    val = val[0].rstrip("/n")
    return val

num = readFile("Resources/08 - Large Number.txt")
print(num)
