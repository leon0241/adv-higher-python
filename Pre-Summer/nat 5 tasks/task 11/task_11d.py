amount = int(input("how many people were out for dinner"))
total = 0

for i in range(amount):
    price = float(input("what was the price of dinner"))
    total = price + total
total = total * 1.1
print(total)
