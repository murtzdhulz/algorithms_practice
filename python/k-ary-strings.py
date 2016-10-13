__author__ = 'Murtaza'

def rangeToList(k):
    result = []
    for i in range(k):
        result.append(str(i))
    return (result)

def mainStrings(n,k):
    if n==0: return[]
    if n==1: return rangeToList(k)
    return [digit+bitstring for digit in mainStrings(1,k) for bitstring in mainStrings(n-1,k)]

print mainStrings(5,3)
