

def makezerostoleft(arr, n):
    l = 0
    for r in range(n):
        if arr[r] != 0 :
            arr[r] , arr[l] = arr[l] , arr[r]
            l += 1
    return arr

print(makezerostoleft([9,0,9,0,4], 5))