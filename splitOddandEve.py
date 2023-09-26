


def segregateEvenOdd(arr, n):
    # code here
    arr.sort()
    arr[:] = [i for i in arr if i %2 == 0] + [i for i in arr if i % 2 != 0]
    print(arr)

segregateEvenOdd([12,34,45,9,8,90,3] ,7)