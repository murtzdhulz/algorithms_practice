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

def max_contiguous_dp(A):
    max_sum=A[0]
    cur_sum=A[0]

    for val in A[1:]:
        cur_sum=max(val,cur_sum+val)
        max_sum=max(max_sum,cur_sum)
    return max_sum

A = [100,3,-16,100,-4,1]
print maxContiguousSum_bad(A)
print maxContiguousSum_better(A)
print max_contiguous_dp(A)