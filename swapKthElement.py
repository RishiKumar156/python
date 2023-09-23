
def swapKthElement(arr,k):
    arr.insert(0,0)
    neg = arr[-k]
    pos = arr[k]
    new_arr = []
    for i in range(len(arr)):
        if arr[i] == pos:
            new_arr.append(arr[pos])
        elif arr[i] == neg:
            new_arr.append(arr[neg])
        else:
            new_arr.append(arr[i])
    print(new_arr[1:])
swapKthElement([5,4,3,7,2,1],3)