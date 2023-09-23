

def leftElement(arr, n):
        for i in range(1, n + 1):
            if len(arr) <= 1:
                break
            if i % 2 != 0:
                mx = max(arr)
                idx = arr.index(mx)
                arr = arr[:idx] + arr[idx+1:] 
            else:
                mi = min(arr)
                idx = arr.index(mi)
                arr = arr[:idx] + arr[idx+1:] 
        print(arr[-1])
    
    
leftElement([7, 8, 3, 4, 2, 9, 5],8)