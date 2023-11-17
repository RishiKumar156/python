def find_vowels(s):
    vowel = []
    for i in s :
        if i in 'aeiou':
            vowel.append(i)
    vowel = vowel[::-1]
    s = list(s)
    for i in range(len(s)):
        if s[i] in 'aeiou':
            s.pop(i)
            s.insert(i , vowel.pop(0))
    s = ''.join(s)
    return s

print(find_vowels('leetcode'))