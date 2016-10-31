__author__ = 'Murtaza'

"""
Given list a,b and an int c
return all (a,b) such that a+b<=c
"""
def find_less(a,b,c):
    count=0
    for val1 in a:
        for val2 in b:
            if val1+val2<=c:
                count+=1
    return count