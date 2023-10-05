

def returnthePeakElement(arr):
    h = {}
    for i in range(len(arr)):
        h[i] = h.get(i , arr[i])
    m = max(h , key= lambda x: h[x])
    return m
print(returnthePeakElement([1,2,4,5]))