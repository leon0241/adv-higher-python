#Write a program that will accept integers input one at a time from the keyboard and save these in an array until the integer -1 is entered

def integers():
    intArray = []
    loop = False
    while loop == False:
        testInt = int(input("enter a whole number"))
        if testInt == -1:
            loop = True;
        else:
            intArray.append(testInt)

integers()
