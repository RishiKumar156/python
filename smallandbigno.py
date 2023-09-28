# Given an array Arr of size N, the array contains numbers in range from 0 to K-1 where K is a positive integer and K <= N. Find the maximum repeating number in this array. If there are two or more maximum repeating numbers return the element having least value.

def maxRepeating(arr):
    # code here
    hashp = {}
    for i in range(len(arr)):
        hashp[arr[i]] = hashp.get(arr[i], 0) + 1
    max_key = max(hashp , key = lambda x: hashp[x])
    m = hashp.get(max_key)
    temp = []
    for v, k in hashp.items():
        if k == m:
            temp.append(v)
    if len(temp) <= 1:
        return temp[0]
    else:
        return min(temp)

ans = maxRepeating([1,1,2,2,0,0])
print(ans)