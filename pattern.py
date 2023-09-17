v = 'geeks'
row = 0 

while row < len(v) + 1:
    k = ''
    for i in range(row):
        k += v[i]
    row += 1
    # print(k)
    
    
length = len(v)

for i in range(length):
    k = ''
    for j in range(length - i):
        k += v[j]
    # print(k)
    
    
def FulColtoSingleCol(avr):
    lng = len(avr)
    for i in range(lng):
        v = ''
        for j in range(lng - i):
            v += avr[j]
        print(v)

FulColtoSingleCol('geeks')