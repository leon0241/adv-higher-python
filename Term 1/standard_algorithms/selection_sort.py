unordered_list = [7,5,9,6,1,8,2,0,3,4]
dummy = "x"
newList = [0] * 10

def selection_sort(list, newList, dummy):
    for i in range(len(list)): #for each value in new list
        min = (len(list)) #length of list(highest) to compare downwards
        minPos = 0 #Resets minimum position
        for j in range(len(list)): #looks for minimum in list
            if list[j] != dummy: #checks if dummy
                if list[j] < min: #Compares it with minimum value
                    min = list[j] #Replaces minimum value if smaller
                    minPos = j #Replaces minumum value position

        newList[i] = list[minPos] #Sets newList[i] to the smallest value in the array
        list[minPos] = dummy #Sets value of current smallest to a dummy value
    return newList

newList = selection_sort(unordered_list, newList, dummy)
print(newList)
