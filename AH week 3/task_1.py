##1.  Create a program that will allow the user to enter and store the data in the table below.  The program should then prompt for a username and use a Linear Search algorithm to find the name in your structure, reporting back with suitable messages to the user.

##2.  Your program should be modular and make use of parameter passing.

def initialise_array():
    class data():
        def __init__(self):
            self.username = str
            self.password = str
            self.email = str
            self.logins = str
    recordData = [data() for i in range(3)]
    return recordData

def get_data(myList):
    for i in range(len(myList)):
        myList[i].username = input("enter a username for person " + str(i + 1) + ": ")
        myList[i].password = input("enter a password for person " + str(i + 1) + ": ")
        myList[i].email = input("enter an email for person " + str(i + 1) + ": ")
        myList[i].logins = input("enter the login number for person " + str(i + 1) + ": ")
    return myList

def get_username(x):
    inputUser = input("enter a username to find: ")
    position = 0
    for i in range(len(x)):
        if inputUser == x[i].username:
            position = i + 1
            break
    return position

def return_info(y, x):
    if x == 0:
        print("no user was found with that name")
    else:
        x -= 1
        print("the users information is: ")
        print("username: " + y[x].username)
        print("password: " + y[x].password)
        print("email: " + y[x].email)
        print("logins: " + y[x].logins)

myData = initialise_array()
myData = get_data(myData)
userPos = get_username(myData)
return_info(myData, userPos)
