firstName = input("what's your first name")
secondName = input("what's your second name")
yob = int(input("what's your year of birth"))

surname = firstName[0:1] + secondName + str(yob)[2:4]
print(surname)
