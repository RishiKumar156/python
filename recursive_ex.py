def funcone():
    print("I'm one")

def functwo():
    funcone()
    print("I'm two")

def functhree():
    functwo()
    print("I'm three")


functhree()
