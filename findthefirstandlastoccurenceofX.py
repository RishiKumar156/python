# Given a sorted array having N elements, find the indices of the first and last occurrences of an element X in the given array.

# Note: If the number X is not found in the array, return '-1' as an array.

def firstAndLast(arr, n, x): 
    # Code here
    if x not in arr:
        return [-1]
    temp = []
    for i in range(len(arr)):
        if arr[i] == x:
            temp.append(i)
    print(temp[0:])

firstAndLast([ 1, 3, 3, 4] , 4, 3)