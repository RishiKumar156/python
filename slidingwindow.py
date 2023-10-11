


def findthesumofitem(arr, k):
    if len(arr) <= 1:
        return False
    total = sum(arr[:k])
    maxt = total
    for i in range(len(arr) - k):
        total -= arr[i]
        total += arr[i+k]
        maxt = max(maxt , total)
    return maxt

print(findthesumofitem([2,3,4,5,6,6] ,3))