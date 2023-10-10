

def reversethegivensubarray(arr, l , r):
    
    if 1 <= l <= r:
        while l < r:
            arr[l-1],arr[r-1] = arr[r-1],arr[l-1]
            l += 1
            r -= 1
    return arr

print(reversethegivensubarray([1, 6, 7, 4] , 1, 4))