def leader(A, N):
    leader = A[-1]
    print(leader)
    found = []
    for i in range(N -1 , -1 , -1):
        if A[i] > leader:
            found.append(A[i])
            leader = A[i]
        print(A[i])
    print(found)
leader([1,2,3, 5,4 ], 4)