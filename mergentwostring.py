# Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.


def solution(s1,s2):
    k = len(s1)+len(s2)
    ans = ''
    for i in range(k):
        if i < len(s1):
            ans += s1[i]
        if i < len(s2):
            ans += s2[i]
    print(ans)
    
solution('hello' , 'world')