# Not solved yet
def isgoodstring(s):
    if len(set(s)) <=1:
        return 'NO'
    c = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] != s[j]: 
                c +=1
                print(s[i] , s[j])
            if c > 3:
                return 'NO'
    return 'YES'

print(isgoodstring(['a','b','a']))