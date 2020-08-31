print("ebic ac test")
points = 0
q1 = input("how many wasps are there per day: ")
if q1 == "5":
    print("correct")
    points += 1
q2 = input("how much is a nook mile ticket: ")
if q2 == "2000":
    print("correct")
    points += 1
q3 = input("what's the museum caretaker called: ")
if q3 == "blathers":
    print("correct")
    points += 1
q4 = input("who's the community's favourite villager: ")
if q4 == "raymond":
    print("correct")
    points += 1
q5 = input("how much stuff can u get from a rock: ")
if q5 == "8":
    print("correct")
    points += 1

if points == 5:
    print("you did well gj")
elif points >= 3:
    print("you did okay")
elif points >= 1:
    print("you did bad")
else:
    print("you failed")
