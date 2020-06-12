valid = False
while valid == False:
    print("What age are you? ")
    age = int(input())
    if age < 0 or age > 120:
        print("age invalid. ")
        print("please enter an age betwewen 0 and 120")
    else:
        valid = True
    print("input is valid")
