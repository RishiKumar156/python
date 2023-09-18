def hashmap(str1, str2):
    deletion = 0
    one = {}
    two = {}
    for char in str1:
        one[char] = one.get(char , 0) + 1
    for char in str2:
        two[char] = two.get(char , 0) + 1
    
    for char in one:
        if char not in two:
            deletion += one[char]
        else:
            deletion += abs(one[char] - two[char])
    
    for char in two:
        if char not in one:
            deletion += two[char]
    
    print(deletion)
    
hashmap('head' , 'bed')