#Linked list simulation

# Create a 2D array as a linked list
LL = [['Alas', 5], ['I', 2], ['Knew', 3], ['him', 4], ['Horatio', -1], ['Poor', 1]]

def print_linked_list(list,link):
    while link != -1: #Loop until end
        item, link = list[link] #Unpack the node
        print(item, end = ' ') #Display the item
    print()

#Main program
print(LL) #Display the linked list

start = 0 #Start is index of first node
print_linked_list(LL, start) #Show list in sequence
