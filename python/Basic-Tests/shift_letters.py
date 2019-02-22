def shift_letters(s,n):
    s=list(s)
    for i,c in enumerate(s):
        s[i]=chr((ord(c)-97+n)%26+97)
    return "".join(s)

print shift_letters("zxcsat",11)

"""
-3: hfkaib
-7: dbgwex
-11: zxcsat
"""


# function to generate letter 'a'
def function_1(v):
    return v+1

def give_me_alphabet():
    l1=[1,2,3,4,5]
    l2=['h','a','n','i','z']

    l3=map(function_1, l1)

    for l,n in zip(l2,l3):
        if n==3:
            return l

print(give_me_alphabet())