import re
def sumOfIntegers(s):
    rst = re.findall(r'\d+',s)
    k = (int(i)for i in rst)
    print(sum(k))

sumOfIntegers('1string34')