def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    m = float("inf")
    for i in range(1,len(arr)-1):
        m = min(m,abs(arr[i]-arr[i+1]))
    return m