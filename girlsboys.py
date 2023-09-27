#this input array does not contain any dupicates so that's girls if it has duplicates then it boys
def girlsandboys(arr):
    j = set()
    for i in arr:
        if i in j:
            return 'BOYS'
        j.add(i)
    return 'GIRLS'

find = girlsandboys([1,2,3,4])
print(find)