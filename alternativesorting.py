def alternateSort(arr, N):
    # Your code goes here
    a = sorted(arr)
    j = a[::-1]
    r = []
    for i in range(len(arr)):
        r.append(j[i])
        r.append(a[i])
    print(r[:N])

alternateSort([7,6,5,4,3,2,1],7)