name = input("what is your name? ")

yearCheck = False
while yearCheck == False:
    year = input("what year are you in? ")
    if year == "1st" or year == "2nd" or year == "3rd" or year == "4th" or year == "5th" or year == "6th":
        yearCheck = True
print("accepted")
