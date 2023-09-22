# Given string s that is appended with a number at last. The task is to check whether the length of string excluding that number is equal to that number.

import re
def findtheLenandFinalItemEquals(s):
    it = re.findall(r'\d+',s)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # upalpha