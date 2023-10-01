def MaximumIntegerValue(s):
    #code here
    j = [int(i) for i in s]
    
    for i in range(len(j)-1):
        # j[i] = j[i]+j[i+1]
        # print(j[i])
        j[i] = j[i]*j[i+1]
        print(j[i])
    return j 

MaximumIntegerValue([0,1,2,3,0])