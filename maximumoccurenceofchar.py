def getMaxOccurringChar(s):
    #code here
    counts = {}
    u = []
    for i in s:
        counts[i] = counts.get(i , 0) + 1
    m = max(counts, key = lambda x: counts[x])
    s = counts.get(m)
    p = []
    for v , k in counts.items():
        if k == s:
            p.append(v)
    return sorted(p)[0]
print(getMaxOccurringChar('testsample'))