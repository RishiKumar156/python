

import re
def themusktrees(s):
    k = re.search('0' ,s)
    print(k.start(), k.end())
    return True

print(themusktrees('00001'))