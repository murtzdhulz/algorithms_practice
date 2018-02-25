def LIS(arr):
    T=[]
    for i in range(len(arr)):
        T.append(1)
        for j in range(i):
            if arr[j]<arr[i]:
                T[i]=max(T[i],T[j]+1)
    max_value=max(T)
    return max_value

def LIS_optimal(arr):
    T = []
    for n in arr:
        if len(T)==0 or n > T[-1]:
            T.append(n)
        else:
            i=0
            j=len(T)-1
            while i<j:
                mid=(i+j)/2
                if n < T[mid]:
                    i = mid+1
                else:
                    j = mid
            T[j]=n
    return len(T)

print LIS([100, -10, 10, 22, 9, 33, 21, 10, 41, 60, 80])
print LIS_optimal([100, -10, 10, 22, 9, 33, 21, 10, 41, 60, 80])