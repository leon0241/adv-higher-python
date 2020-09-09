#Linked list simulation

# Create a 2D array as a linked list
LL = [['Zero', 1], ['One', 2], ['Two', -1]]

def print_linked_list(list,link):
    while link != -1: #Loop until end
        item, link = list[link] #Unpack the node
        print(item, end = ' ') #Display the item
    print()

#Main program
print(LL) #Display the linked list

start = 0 #Start is index of first node
print_linked_list(LL, start) #Show list in sequence
