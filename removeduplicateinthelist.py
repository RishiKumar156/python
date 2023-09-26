
def removeDuplicate(A):
    seen = set()
    r = [i for i in A if i not in seen and not seen.add(i)]
    print(r)

removeDuplicate([1,1,2,3,3,4,5,5,6])