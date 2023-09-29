# need to rotate the input array in to the leeft side 

def leftRotate(arr, k):
    # Your code goes here
    arr[k:] + arr[:k]
    return arr

t = leftRotate([80, -62 ,-90 ,7, 50 ,-41 ,70 ,8 ,-7, -9 ,44, 22 ,-57 ,-97 ,26 ,72 ,95, -39 ,65 ,-51, 52, -29, -18, 4, 98 ,-3 ,95, -11 ,-90] , 9944)

print(t)