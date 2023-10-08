

def countWrongPlacedBalls(s):
    # code here
    c = 0
    for i in range(len(s)):
        if s[i] == 'R' and i % 2 != 0:
            c += 1
        elif s[i] == 'B' and i % 2 == 0:
            c += 1
    return c

print(countWrongPlacedBalls('RBRB'))