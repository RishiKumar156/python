
import re
def findthepal(s):
    k = re.finditer('[a-zA-Z]' , s)
    j = ''
    for i in k:
        j += i.group(0)
    if j != j[::-1]:
        print(type(j[::-1]))
    return True
print(findthepal('12rewser1'))