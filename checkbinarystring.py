

import re
def check(s):
    if len(set(s)) <= 1:
        return 'VALID'
    k = re.finditer('1' , s)
    j = [i.group() for i in k]
    # y = s[:j[0]] + s[j[-1]:]
    return  j
print(check('100111011'))