

def CompleteTheSkills(a,b):
        A = 0 
        B = 0 
        k = [i for i in a]
        j = [i for i in b]
        for i in range(len(k)):
            if k[i] > j[i]:
                A += 1
            if k[i] < j[i]:
                B += 1
        print(A,B)

CompleteTheSkills({5,6,7} ,{7,6,8})