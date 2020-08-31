count = 0
input1 = input("do you take english? ")
if input1 == "yes":
    count += 1
input2 = input("do you take drama? ")
if input2 == "yes":
    count += 1
input3 = input("do you take music? ")
if input3 == "yes":
    count += 1

if count >= 2:
    print("you are eligible")
