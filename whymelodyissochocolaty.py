

def findthechocolate(arr):
    m = float('-inf') #initial value is negative 
    for i in range(len(arr) -1):
        if arr[i] + arr[i +1] > m :
            m = arr[i] + arr[i +1]
    return m


print(findthechocolate([1,2,3,4,5,6]))