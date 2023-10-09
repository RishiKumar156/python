

def getCount (S, N):
    # your code here
    k = {}
    for i in S:
        k[i] = k.get(i , 0) + 1
    c = 0
    for k , v in k.items():
        print(v)
        if v % N == 0:
            c += 1
    return c

print(getCount('abc' , 1))