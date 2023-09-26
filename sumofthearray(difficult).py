def divideArrayElements(arr, k):
    r = []
    for i in arr:
        c= 0 
        while i >= k:
            i -= k 
            if i >0:
                c += 1
        r.append(c)
    return r

# Example usage:
arr = [5, 8, 24]
k = 3
result = divideArrayElements(arr, k)
print(result)
