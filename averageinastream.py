
def avarageInAStream(arr):
    count = 0
    track = 0
    done = []
    for i in arr:
        track += i
        count += 1
        average = track /count 
        done.append(average)
    print(done)
    
avarageInAStream([20,20,30,40])