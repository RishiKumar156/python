# Given an integer array Arr of size N. For each element in the array, check whether the right adjacent element (on the next immediate position) of the array is smaller. If next element is smaller, update the current index to that element. If not, then  -1.

def smaller(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr[i] = arr[i+1]
        else :
            arr[i] = -1
    arr[-1] = -1
    print(arr)

smaller([4,2,1,5,3])