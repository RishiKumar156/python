
import re
def findthemax(s):
    k = re.findall(r'\d+' , s)
    j = [int(i) for i in k]
    if len(k) <= 0:
        return -1
    return max(j)

print(findthemax('hvcl5bcwhagmx28lmyngo10s29wlhirzgqnvenjn5ldt4erri03ty5zt4c2mleuniseclia'))