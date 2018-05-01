import itertools

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        N = len(s)
        mask = [False] * N
        for i in xrange(N):
            s_cur = s[i:]
            for word in dict:
                if s_cur.startswith(word):
                    for j in xrange(i, min(i + len(word), N)):
                        mask[j] = True

        ans = []
        # Now mask is ready to be used
        for flag, grp in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if flag: ans.append("<b>")
            ans.extend([z[0] for z in grp])
            if flag: ans.append("</b>")
        return "".join(ans)

"""
Given a string s and a list of strings dict, 
you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
"""