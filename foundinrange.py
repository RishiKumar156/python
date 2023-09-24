
# Given an array arr[] containing positive elements. A and B are two numbers defining a range. The task is to check if the array contains all elements in the given range.
def foundData(arr,A,B):
    element_set = set(arr)
    for i in range(A,B+1):
        if i not in element_set:
            return False
    return True
foundData([1, 4, 5, 2, 7, 8, 3] , 2,6)