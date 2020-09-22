#Simple Binary Search in Python
A = [1,3,5,7,8,9,11,34,45] #Array must be in order
key = 3 #The integer to search for in the array

comparisons = 0

def binary_search(list, target):
    iMax = len(list) - 1 #Upper limit for zero based array
    iMin = 0 #Lower limit for zero based array
    iMid = 0 #Will be mid point between limits
    global comparisons #Made global so it can be removed
    while (iMax >= iMin):
        iMid = int((iMax + iMin)/2) #Must change to an integer to use as an index
        print(iMax, iMid, iMin)
        comparisons += 1
        if A[iMid] == target:
            return iMid
            break #Need to quit from loop when found
        elif A[iMid] < target:
            iMin = iMid + 1 #Move the lower limit
        else:
            iMax = iMid - 1 #Move the upper limit

    #Main program
position = binary_search(A, key)
print(position)
if position == None:
    print("Target not found")
else:
    print("Target found in element",position, "of the array")
print("Number of comparisons =", comparisons)
