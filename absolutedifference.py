# Given an array of sorted integers. The task is to find the closest value to the given number in array. Array may contain duplicate values.


def findClosest(arr, n, target):
    dif = {}  # A dictionary to store the absolute differences between array elements and the target
    for i in range(len(arr)):
        df = abs(arr[i] - target)  # Calculate the absolute difference
        dif[arr[i]] = df  # Store the absolute difference

    f = {}  # A dictionary to store the frequency of absolute differences of 1
    for v, k in dif.items():
        if k == 0:
            return v
        elif k == 1:
            f[v] = f.get(v, 0) + 1  # Only count absolute differences of 1

    if not f:
        return None  # Handle the case when there are no absolute differences of 1

    m = max(f, key=lambda x: f[x])
    return m

# Input values
n = 15
target = 11
arr = [0, 1, 2, 3, 3, 5, 5, 7, 8, 9, 12, 12, 13, 14, 16]

# Call the findClosest function
result = findClosest(arr, n, target)

# Print the result
print(result)

# test = findClosest([1 ,4 ,4 ,5 ,6 ,7 ,7 ,9 ,10 ,10 ,10 ,11 ,11 ,12 ,13 ,15 ,15 ,19 ,19] , 10)
# print(test)