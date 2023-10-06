
import re
def binary(arr):
    x = re.finditer('0' , arr)
    idx = []
    for i in x:
        idx.append(i.start())
        idx.append(i.end())
    return sorted(set(idx))

print(binary('1100011'))