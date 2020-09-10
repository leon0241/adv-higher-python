#What would be the linked list for..
#'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'red', 'The', 'the'
#... to create the sentence...
#'The quick brown fox jumps over the lazy dog'

linkedList = [
    ["brown", 2], #0
    ["dog.", -1], #1
    ["fox", 3], #2
    ["jumps", 5], #3
    ["lazy", 7], #4
    ["over", 9], #5
    ["quick", 0], #6
    ["red", 1], #7
    ["The", 6], #8
    ["the", 4] #9
]

def print_linked_list(list, link):
        while link != -1: #Loop until end
            item, link = list[link] #Unpack the node
            print(item, end = ' ') #Display the item
        print()

start = 8
print_linked_list(linkedList, start)
