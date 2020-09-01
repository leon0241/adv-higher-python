#Write a Program to accept 10 strings input one at a time from the keyboard and add them to an array and then display the entries in reverse order
LIST_SIZE = 10

def enter_strings(myList):
    for i in range(LIST_SIZE):
        myList[i] = input("Enter a string: ")
    return myList

def reverse_strings(myList):
    reverseList = [""] * LIST_SIZE
    for i in range(LIST_SIZE):
        reverseList[i] = myList[(LIST_SIZE - 1) - i]
    return reverseList

def print_array(myList):
    for i in range(LIST_SIZE):
        print(myList[i])

stringArray = [""] * LIST_SIZE
stringArray = enter_strings(stringArray)
stringArray = reverse_strings(stringArray)
print_array(stringArray)
