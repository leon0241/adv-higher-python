 #1.  Create a program that will allow the user to enter and store the data in the table below.  The program should then prompt for a value for copies available and make use of a Counting Occurences algorithm algorithm to display the Name, ISBN and Copies available for those records where Copies available = 16.

#2.  Your program should be modular and make use of parameter passing.

def initialise_array():
    class data():
        def __init__(self):
            self.name = str
            self.isbn = str
            self.copies = int
    recordData = [data() for i in range(4)]
    return recordData

def get_data(x):
    for i in range(len(x)):
        x[i].name = input("enter a name for book " + str(i + 1) + ": ")
        x[i].isbn = input("enter an ISBN for book " + str(i + 1) + ": ")
        x[i].copies = int(input("enter the copies available for book " + str(i + 1) + ": "))
    return x

def get_copies(x):
        copyInput = int(input("enter a value for the copies available: "))

def find_records(x):
    filteredRecords = []
    for i in range(len(x)):
        if x[i].copies == 16:
            filteredRecords.append(i)
    return filteredRecords

def display_data(x, y):
    for i in range(len(x)):
        print("name: " + y[x[i]].name)
        print("ISBN: " + y[x[i]].isbn)
        print("copies: " + str(y[x[i]].copies))

data = initialise_array()
data = get_data(data)
get_copies(data)
filteredRecords = find_records(data)
display_data(filteredRecords, data)
