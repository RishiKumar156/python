

def rearrange(arr):
    k = sorted(arr)
    j = k[::-1]
    u = len(arr)
    for i in range(len(arr)):
        arr.append(k[i])
        arr.append(j[i])
    arr[:] = arr[u:u+u]
    return arr
item = rearrange([1,2,3,4,5,6,7,8,9,10])
print(item)