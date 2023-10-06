def ispar(x):
    # code here
    stack = []
    for i in x:
        if i in '{[(':
            stack.append(i)
        else :
            if not stack:
                return False
            j = stack.pop()
            if j == '{' and i != '}' or j == '[' and i != ']' or j == '(' and i != ')':
                return False
    if stack :
        return False
    return True

print(ispar(['(' , ')' , '{' , '}' , ')']))