# A good implementation also in Karumanchi - Pg 365
# lps indicates longest proper prefix which is also suffix.. A proper prefix is prefix with whole string not allowed.

def compute_lps(pat):
    lps = [0]*len(pat)
    i=1
    l=0
    while i<len(pat):
        if pat[i]==pat[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
    return lps

# I prefer this one since it is more sleek
def compute_lps2(pat):
    lps=[0]*len(pat)
    for i in xrange(1, len(lps)):
        t = lps[i-1]
        while t>0 and pat[i]!=pat[t]:
            t=lps[t-1]
        if pat[i]==pat[t]:
            t+=1
        lps[i]=t
    return lps

def kmp(pat, text):
    lps = compute_lps2(pat)
    print(lps)
    i=j=0

    while i<len(text):
        if pat[j]==text[i]:
            i+=1
            j+=1
            if j==len(pat):
                print("Pattern found at:", (i-j))
                # reset j - only move as much as you need and not more
                j = lps[j-1]
        else:
            if j!=0:
                j=lps[j-1]
            else:
                # Since at this point we are at the start of the pattern, you want to go on to the next character
                i+=1

# txt = "AAAAAAAAAAAAAABX"
# pat = "AAA"
# txt = "ABABDABACDABABCABABKL"
# pat = "ABABCABAB"
txt="ABCTTTT"
pat="BCABCBC"
kmp(pat, txt)