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

print longest_substring_k_distinct("eceba",2)