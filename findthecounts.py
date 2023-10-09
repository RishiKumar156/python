

def found(arr, cnt):
    h = {}
    for i in arr:
        h[i] = h.get(i , 0) + 1
    n = []
    for k , v in h.items():
        if v == cnt:
            n.append(k)
    return sorted(n)[0] , h

print(found([3,5,5,3,2],1))