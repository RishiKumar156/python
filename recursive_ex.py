def funcone():
    print("I'm one")

def functwo():
    funcone()
    print("I'm two")

def functhree():
    functwo()
    print("I'm three")


functhree()

"""Factotail function recustsion this action should do the same thing repeatedly and should get reduced by the value theres is a recursion condition is to follow the same rules for each call's """
def factorial(n):
    if n== 1:
        return 1 
    return n * factorial(n-1)

print(factorial(4))