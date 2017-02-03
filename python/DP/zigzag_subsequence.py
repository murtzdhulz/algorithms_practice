__author__ = 'Murtaza'

def zigzag_subsequence(A):
    n=len(A)

    # We want a lookup having 2 columns and n rows, one for positive difference, one for negative difference (like coming from the prev element. And then we set the ith entry looking behind
    # Can easily switch between rows and columns (that's how I like imagining it)
    table=[[0]*2 for _ in range(n)]

    table[0][0]=1
    table[0][1]=1
    best=1

    for i in xrange(n):
        for j in xrange(i-1,-1,-1):
            if A[i]>A[j]:
                table[i][0]=max(table[j][1]+1,table[i][0])
            elif A[i]<A[j]:
                table[i][1]=max(table[j][0]+1,table[i][1])
        best=max(table[i][0],table[i][1],best)

    return best

A=[1, 7, 4, 9, 2, 5 ]
print zigzag_subsequence(A)