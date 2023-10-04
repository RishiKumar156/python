

def changeToRoman(arr):
        k = { 'I' : 1 , 'V' : 5 , "X" : 10 , "L": 50 , 'C' : 100, 'D' : 500 ,'M' : 1000 }
        t = 0
        prev = 0
        for symbol in arr:
                value = k[symbol]
                if value < prev :
                        t -= value
                else :
                        t += value
                        prev += value
        return t

print(changeToRoman(['X',  'I' ,'V']))