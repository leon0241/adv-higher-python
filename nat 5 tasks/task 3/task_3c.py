amount = int(input("how much money do you want to borrow "))
time = int(input("how many months do you want to repay it for "))
intAmount = amount * 1.15
payment = intAmount / time
print("your monthly payments are " + str(payment))
