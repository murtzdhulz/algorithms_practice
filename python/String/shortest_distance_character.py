class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n=len(S)
        res=[n]*n
        pos= -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C: pos=i
            res[i]=min(res[i],abs(i-pos))
        return res

"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""