

# we have to return the anagram of the two arr
from collections import Counter
def anagram(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    if c1 != c2:
        return 0
    return 1

print(anagram([1,3,45,32,334] , [3,2,42,5,34,5]))