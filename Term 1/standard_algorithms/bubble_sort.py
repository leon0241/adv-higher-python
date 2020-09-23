unordered_list = [7,5,9,6,1,8,2,0,3,4]
newList = [0] * 10

def swap(item1, item2):
    return item2, item1

def bubble_sort(list):
    swaps = 0
    comparisons = 0
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            comparisons = comparisons + 1
            if list[i - 1] > list[i]:
                list[i - 1], list[i] = swap(list[i - 1], list[i])
                swaps += 1
                swapped = True
        print(list)
    print("Number of swaps made =", swaps)
    print("Number of comparisons =", comparisons)

print(unordered_list)
bubble_sort(unordered_list)
print(unordered_list)
