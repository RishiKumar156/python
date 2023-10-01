

def isPossible(self, s):
    hp = {}
    for i in s:
        hp[i] = hp.get(i ,0)+ 1
    c = 0 
    for k , v in hp.items():
        if v % 2 != 0 :
            c += 1
        if c > 1:
            return 0
    return 1
print(isPossible('geeksforgeeks'))