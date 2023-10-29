

def bubble_sort(item):
    for j in range(len(item)-1):
        for i in range(len(item) -1):
            if item[i] > item[i+1]:
                item[i] , item[i+1] = item[i+1], item[i]
    return item

print(bubble_sort([3,4,5,2,1]))