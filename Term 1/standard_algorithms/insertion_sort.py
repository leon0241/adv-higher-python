unordered_list = [7,5,9,6,1,8,2,0,3,4]
newList = [0] * 10

def swap(item1, item2):
    return item2, item1

def insertion_sort(list):
    max = len(list)
    comparisons = 0
    swaps = 0
    for i in range(1, max):
        comparisons += 1
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = swap(list[j - 1], list[j])
            swaps += 1
            j -= 1
            print(list)
    print("Number of swaps made =", swaps)
    print("Number of comparisons =", comparisons)

print(unordered_list)
insertion_sort(unordered_list)
