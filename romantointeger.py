

def changeromantoint(s):
    k = { 'I' : 1 , 'V' : 5 , "X" : 10 , "L": 50 , 'C' : 100, 'D' : 500 ,'M' : 1000}
    
    ct= 0
    pv_t = 0
    
    for i in reversed(s):
        if k[i] < pv_t :
            ct -= k[i]
        else:
            ct += k[i]
            pv_t = k[i]
    return ct


print(changeromantoint('XIV'))