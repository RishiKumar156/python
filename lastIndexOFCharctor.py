# Given a string S  and a character X, the task is to find the last index (0 based indexing) of X in string S. If no index found then the answer will be -1.

def LastIndex(s,p):
    idx = -1
    for i in range(len(s)):
        if s[i] == p:
            idx = i
    print(idx)
LastIndex('peelo', 'z')