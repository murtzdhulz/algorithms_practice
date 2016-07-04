__author__ = 'Murtaza'

def LCS(X,Y):
    n=len(X)
    m=len(Y)
    L=[[0]*(m+1) for i in xrange(n+1)]
    # print 'Initial matrix:',L
    # L[n][m]=1
    # print L
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            if X[i-1]!=Y[j-1]:
                L[i][j]=max(L[i-1][j],L[i][j-1])
            else:
                L[i][j]=L[i-1][j-1]+1
    return L[n][m]

X='BCDBCDA'
Y='ABECBA'

print LCS(X,Y)