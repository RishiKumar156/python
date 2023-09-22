# Given string s that is appended with a number at last. The task is to check whether the length of string excluding that number is equal to that number.

import re
def findtheLenandFinalItemEquals(s):
    it = re.findall(r'\d+',s)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    upalpha = alpha.upper()
    k = ''
    for i in s:
        if i in upalpha or i in alpha:
            k += i
    
    if len(k) == int(it[0]):
        print(1)
    else :
        print(0)
        
findtheLenandFinalItemEquals('hello5')