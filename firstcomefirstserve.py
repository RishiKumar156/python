# this code retuns that k value which occur first 

def firstElement(arr,k): 
    heap = {}
    for i in range(len(arr)):
        heap[arr[i]] = heap.get(arr[i] , 0) + 1
    for i in range(len(arr)):
        if heap.get(arr[i]) == k:
            return arr[i]
    return -1

found = firstElement([1,7,4,7,4,3,8] , 2)

print(found)