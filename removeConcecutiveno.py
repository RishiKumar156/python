

def removetherightnextsameno(N):
        n = str(N)
        k = ''
        for i in range(len(n)):
            if i == 0 or n[i] != n[i-1]:
                k += n[i]
        return k

print(removetherightnextsameno([1,2,2,4]))    