

def removeElement(arr,v):
    arr[:] = [k for k in arr if k != v]
    return arr
print(removeElement([1,2,1,3,4,5] , 1))