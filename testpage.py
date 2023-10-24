# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
def longest_consecutive_sequence(sets):
    s = sorted(sets)
    for i in range(len(sets)):
        current = s[i]
        if current + 1 != s[i+1]:
            print(current , s[i+1])
            return False 
        print(current+1 , s[i+1])
print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""