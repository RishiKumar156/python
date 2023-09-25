

def nextGreatest(arr, n):
    f = []
    for i in range(len(arr)):
        temp = arr[i:]
        f.append(max(temp))
    f.append(-1)
    print(f[1:])

nextGreatest([2, 3, 1, 9],4)