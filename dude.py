box1 = ['a', 3, 'c' , 'r', 'e']
box2 = ['a', 3, 'c', 'r', 't']

def check_the_strak(box1,box2):
    hash_table = {}
    for i in range(len(box1)):
        hash_table[box1[i]] = hash_table.get(box1[i], 0) + 1
    
    for i in range(len(box2)):
        hash_table[box2[i]] = hash_table.get(box2[i], 0) + 1
    
    for k , v in hash_table.items():
        if v >=2 :
            print(k,v)
    return True
# print(check_the_strak(box1, box2))

def sum_of_the_two_value(arr, sum):
    table = {}
    for i in range(len(arr)):
        s = sum - arr[i]
        if s in table:
            return table[s] , arr[i] , table
        table[arr[i]] = arr[i]
    return False
print(sum_of_the_two_value([6,4,3,2,1,7], 9))
print(sum_of_the_two_value([1,2,4,4], 8))
print(sum_of_the_two_value([1,2,4,4], 16))


def reverse_string(item):
    if not item:
        return False
    return item[::-1] 

print(reverse_string(''))

def merge_sorting(grp1, grp2):
    j = grp1 + grp2
    return sorted(j)

print(merge_sorting([1,3,5], [2,4,6]))