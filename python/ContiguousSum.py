__author__ = 'Murtaza'

def maxContiguousSum_bad(A):
    maxsum = float('-inf')
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            cursum = 0
            for k in range(i,j+1):
                cursum+=A[k]
                if cursum>maxsum:
                    maxsum=cursum
    return maxsum

def maxContiguousSum_better(A):
    maxsum = float('-inf')
    n = len(A)
    for i in range(n):
        cursum = 0
        for j in range(i,n):
                cursum+=A[j]
                if cursum>maxsum:
                    maxsum=cursum
    return maxsum

A = [100,3,-16,100,-4,1]
print maxContiguousSum_bad(A)
print maxContiguousSum_better(A)