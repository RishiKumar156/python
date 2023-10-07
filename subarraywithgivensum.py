

def subarraywithgivensum(arr,n):
    c_s = sum(arr[:n])
    r = [c_s]
    for i in range(1,len(arr)-n+1):
        c_s = arr[i-1]
        c_s = arr[i+n -1]
        r.append(c_s)
    return sum(r)

print(subarraywithgivensum([1,2,3,4,5], 3))