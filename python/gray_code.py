__author__ = 'Murtaza'

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans=[]
        for i in xrange(2**A):
            print 'i is:',i
            print 'Shifted i is',i>>1
            ans.append((i>>1)^i)
        print ans
        return ans

ans=Solution()
ans.grayCode(3)