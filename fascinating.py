# Given a number N. Your task is to check whether it is fascinating or not.
# Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3, and when both these products are concatenated with the original number, then it results in all digits from 1 to 9 present exactly once.


def fascinating(n):
    # code here
    if len(str(n)) < 3:
        print('Not Fascinating')
    
    concatenate = str(n) + str(n*2) + str(n*3)
    no = '123456789'
    check = ''
    for i in concatenate:
        if i in no and i not in check:
            check += i
        else :
            print("Not Fascinating")
    print('Fascinating')

fascinating(192)