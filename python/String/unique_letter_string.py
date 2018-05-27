from collections import defaultdict
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        index=defaultdict(list)
        for i,c in enumerate(S):
            index[c].append(i)
        res=0
        for L in index.values():
            L = [-1] + L + [len(S)]
            for i in xrange(1,len(L)-1):
                res+=(L[i]-L[i-1])*(L[i+1]-L[i])
        return res%(10**9+7)

"""
A character is unique in string S if it occurs exactly once in it.

For example, in string S = "LETTER", the only unique characters are "L" and "R".

Let's define UNIQ(S) as the number of unique characters in string S.

For example, UNIQ("LETTER") =  2.

Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.

If there are two or more equal substrings at different positions in S, we consider them different.

Since the answer can be very large, retrun the answer modulo 10 ^ 9 + 7.

 

Example 1:

Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.
"""