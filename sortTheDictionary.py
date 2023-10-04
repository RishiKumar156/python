

def sortetheDict(arr):
    check = {')': '(' , '}':'{' , ']':'['}
    stack = []
    for i in arr:
        if i not in check.values():
            stack.append(i)
        elif i not in check.keys():
            if not stack or stack.pop() != check[i]:
                return False
    return stack
print(sortetheDict(['{' , '}' , '(' , ')' , ']' , '[']))