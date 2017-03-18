__author__ = 'Murtaza'

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n=len(words)
        if n==0 or n!=len(words[0]):
            return False

        for i in xrange(n):
            for j in xrange(len(words[i])):
                if j>=n or len(words[j])<=i or words[i][j]!=words[j][i]:
                    return False
        return True

