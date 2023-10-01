

def check(arr):
    h = {}
    for i in arr:
        h[i] = h.get(i , 0) + 1
    
    for k ,v in h.items():
        print(k , v)
        # if v % 2 != 0:
        #     return False
    # return True

print(check('[]{}['))