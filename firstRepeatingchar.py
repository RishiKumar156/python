def firstrepeatingchar(A):
    hashmap = {}
    for i in A:
        hashmap[i] = hashmap.get(i , 0) + 1
    
    for i in range(len(A)):
        if A[i] in hashmap:
            if hashmap[A[i]] > 1:
                return print(A[i])
    return print("-1")
    
firstrepeatingchar('geeksforgeeks')
    