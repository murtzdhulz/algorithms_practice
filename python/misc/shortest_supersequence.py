__author__ = 'Murtaza'

def find_s_supersequence(big_arr,small_arr):
    closures=get_closures(big_arr,small_arr)
    print closures
    return shortest_sequence(closures)

def get_closures(big_arr,small_arr):
    closures=[0]*len(big_arr)
    for val in small_arr:
        sweep_for_closure(big_arr,closures,val)
    return closures

def sweep_for_closure(b,c,val):
    next=-1
    for i in range(len(b)-1,-1,-1):
        if b[i]==val:
            next=i
        if (next==-1 or c[i]<next) and (c[i]!=-1):
            c[i]=next

def shortest_sequence(closure):
    start,end=0,closure[0]
    for i in range(1,len(closure)):
        if closure[i]==-1:
            break
        if (closure[i]-i)<(end-start):
            start,end=i,closure[i]

    return start,end,-1 if end==-1 else end-start+1

big=[7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small=[1,5,9]
print find_s_supersequence(big,small)