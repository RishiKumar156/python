

def wrongball(s):
    c = 0
    for i in range(len(s)-1):
        if s[i] == 'R' and s[i +1] == 'R' or s[i] == 'B' and s[i + 1] == 'B':
            c += 1
    return c

print(wrongball('BBBBRBR'))