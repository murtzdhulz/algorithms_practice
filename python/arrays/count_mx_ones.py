# Program to return the max count of 1s in any row, column, diagonol (consider all diagonals)

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        m, n = len(M), len(M[0])
        rc=[0]*m
        cc=[0]*n
        diag, ad = [0]*(n+m-1), [0]*(n+m-1)
        for i in xrange(m):
            for j in xrange(n):
                if M[i][j]==1:
                    rc[i]+=1
                    cc[j]+=1
                    diag[m-i+j-1]+=1
                    ad[i+j]+=1
        return max([max(rc), max(cc), max(diag), max(ad)])