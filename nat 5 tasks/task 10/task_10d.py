name = input("what is your name? ")

check = False
while check == False:
    gender = input("what is your gender? ")
    if gender == "male" or gender == "female":
        check = True

check = False
while check == False:
    age = int(input("what is your age? "))
    if age > 0 and age < 120:
        check = True
