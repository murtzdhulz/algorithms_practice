__author__ = 'Murtaza'
from collections import defaultdict

def longest_substring_k_distinct(s,k):
    i=0
    length=0
    d=defaultdict(int)

    for j in range(len(s)):
        d[s[j]]+=1
        # can do this part with pointers too but this is easier
        while len(d)>k:
            d[s[i]]-=1
            if d[s[i]]==0:
                del d[s[i]]
            i+=1
        length=max(length,j-i+1)
    return length

"""
The idea here is:
In a dictionary keep track of the rightmost position of each character in a string.
When you dictionary becomes bigger than k, find the righmost occurence of the oldest character that occurred and delete
the entry. 
Update start position by incrementing it by 1
Keep calculating res
"""
def lengthOfLongestSubstringKDistinct_optimal(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    start = 0
    res = 0
    d = {}
    for i, c in enumerate(s):
        # Track the rightmost position of the current character in the string
        d[c] = i
        # print d
        if len(d) > k:
            start = min(d.values())
            del d[s[start]]
            start += 1
        res = max(res, i - start + 1)
        # print "Res is:", res
    return res

print lengthOfLongestSubstringKDistinct_optimal("eceba",2)

# ex: "aeeaaabc"