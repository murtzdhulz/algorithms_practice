def LIS(arr):
    T=[]
    for i in range(len(arr)):
        T.append(1)
        for j in range(i):
            if arr[j]<arr[i]:
                T[i]=max(T[i],T[j]+1)
    max_value=max(T)
    return max_value

print LIS([100, -10, 10, 22, 9, 33, 21, 10, 41, 60, 80])
