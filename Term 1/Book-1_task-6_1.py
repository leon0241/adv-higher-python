#What would be the linked list for..
#'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'red', 'The', 'the'
#... to create the sentence...
#'The quick brown fox jumps over the lazy dog'

linkedList = [
    ["brown", 9], #0
    ["dog.", -1], #1
    ["fox", 4], #2
    ["jumps", 5], #3
    ["lazy", 8], #4
    ["over", 6], #5
    ["quick", 2], #6
    ["red", 3], #7
    ["The", 1], #8
    ["the", 7] #9
]

def print_linked_list(list, link):
    newLink = 0
    stop = 0
    while link != -1 and stop < 20: #Loop until end
        for i in range(len(list)):
            if list[i][1] == link + 1:
                newLink = i

        item, link = list[newLink] #Unpack the node
        print(item, end = ' ') #Display the item
        stop += 1
    print()

start = 0
print_linked_list(linkedList, start)
