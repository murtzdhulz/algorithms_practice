__author__ = 'Murtaza'

def rangeToList(k):
    result = []
    for i in range(k):
        result.append(str(i))
    return result

def mainStrings(n,k):
    if n==0: return[]
    if n==1: return rangeToList(k)
    return [digit+bitstring for digit in mainStrings(1,k) for bitstring in mainStrings(n-1,k)]

print mainStrings(3,2)

# Generating XOR data
# for s in mainStrings(7,2):
#     cur_l=list(int(s_cur) for s_cur in s)
#     cur_sum=0
#     for val in cur_l:
#         cur_sum+=val
#     if cur_sum%2==0:
#         cur_l.append(0)
#     else:
#         cur_l.append(1)
#
#     print cur_l
