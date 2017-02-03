__author__ = 'Murtaza'

def LCSubsequence(X,Y):
    n=len(X)
    m=len(Y)
    L=[[0]*(m+1) for _ in xrange(n+1)]
    # print 'Initial matrix:',L
    # L[n][m]=1
    # print L
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            if X[i-1]!=Y[j-1]:
                L[i][j]=max(L[i-1][j],L[i][j-1])
            else:
                L[i][j]=L[i-1][j-1]+1
    print 'The LCSubsequence string is:'
    print_LCSubsequence(L,X,Y,n,m)
    print
    print 'Length of LCSubsequence is:',L[n][m]
    for line in L:
        print line

def LCSubstring(X,Y):
    n=len(X)
    m=len(Y)
    L=[[0]*(m+1) for _ in xrange(n+1)]
    # print 'Initial matrix:',L
    # L[n][m]=1
    # print L
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            if X[i-1]!=Y[j-1]:
                L[i][j]=0
            else:
                L[i][j]=L[i-1][j-1]+1

    max=0
    for val in L:
        for each_val in val:
            if each_val>max:
                max=each_val

    print 'Length of LCSubstring is:',max

def print_LCSubsequence(L,X,Y,i,j):
    # print 'In Print:',i,j
    if L[i][j]==0:
        return
    if X[i-1]==Y[j-1]:
        print_LCSubsequence(L,X,Y,i-1,j-1)
        print X[i-1],
        return
    if X[i-1]!=Y[j-1] and L[i][j]==L[i-1][j]:
        print_LCSubsequence(L,X,Y,i-1,j)
        return
    if X[i-1]!=Y[j-1] and L[i][j]==L[i][j-1]:
        print_LCSubsequence(L,X,Y,i,j-1)
        return

X='BCDBCDA'
Y='ABECBA'
LCSubsequence(X,Y)

X='BCDBCDA'
Y='ABECDAPL'
LCSubstring(X,Y)