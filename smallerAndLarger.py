# Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X and elements more than or equal to X. 

def smallerAndLarger(array, x):
    for i in range(len(array)):
        gt = 0
        sl = 0
        if int(array[i]) <= x:
            gt += 1
        # trick is using two if statements instead of elif 
        if int(array[i]) >= x:
            sl += 1
    print(gt, sl)
    
smallerAndLarger([3,3,3] , 3)