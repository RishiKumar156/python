
test = [1,2,3,5]

l = 0 
r = len(test) - 1

while l < r:
    mid = (l + r) // 2
    if test[mid] == mid :
        r = mid - 1
    else :
        l = mid + 1 
    print(mid)
    break