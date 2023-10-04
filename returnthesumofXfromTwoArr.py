

def returnTheSomeOFArr(A,B,X):
    set_b = set(B)
    s = []
    for i in range(len(A)):
        com = X -A[i]
        if com in set_b:
            s.append((A[i] , com))
    s.sort(key = lambda x :x[0])
    return s

print(returnTheSomeOFArr([1, 2, 4, 5, 7] , [5, 6, 3, 4, 8] ,9))