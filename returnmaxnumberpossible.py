# need to return the maximum possible number of the given array


def MaxNumber(arr, n):
    #code here.
    arr = sorted(arr)[::-1]
    j = ''.join(map(str, arr))
    return j

ans = MaxNumber([9,2,3,4,5], 5)
print(ans)