


def findthekswaps(s,k):
    s = list(s)
    j = -1
    for i in range(k+1):
        s[i] , s[j] = s[j], s[i]
        j -= 1
    return s


def findlen(s):
    k = 0
    for i in s:
        if i not in 'aeiou':
            k += 1
    if k % 2 != 0:
        return 'HE!' , k
    else:
        return 'SHE!' , k

print(findlen('eurrgmfsyhoqoyawlfbmdifcxucmkcxoxoidapwywkrkkriw'))
print(findthekswaps('1234567' , 4))