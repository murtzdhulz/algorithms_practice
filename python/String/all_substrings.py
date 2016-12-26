__author__ = 'Murtaza'

def all_substrings(s):
    n=len(s)
    res=[]
    for i in range(n):
        for j in range(i+1,n+1):
            res.append(s[i:j])
    return res

k=all_substrings("Parrot")
print k