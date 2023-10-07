


def checkthecontinusno(arr):
    minx = min(arr)
    mx = max(arr)
    for i in range(minx ,mx):
        print(i)
        if i not in arr:
            return False
    return True

print(checkthecontinusno([1,2,4,5]))