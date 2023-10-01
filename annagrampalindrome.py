

def anagrampalindrome(s):
    hashp = {}
    for i in s:
        hashp[i] = hashp.get(i , 0) + 1
    m = max(hashp , key = lambda x: hashp[x])
    j = hashp.get(m)
    c = 0
    for v , k in hashp.items():
        if k == 1:
            c += 1
        if c > 1:
            return 'No'
    return 'yes'

print(anagrampalindrome('geeksforgeeks'))