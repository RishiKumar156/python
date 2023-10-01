def findsubs(arr):
    k = []
    for outer in range(len(arr)):
        for inner in range(outer+1 , len(arr)+1):
            print(arr[outer:inner])
        k.append(arr[outer:inner])
    return k

found = findsubs([1,1,1,1])
print(found)