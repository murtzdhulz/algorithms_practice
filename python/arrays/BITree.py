__author__ = 'Murtaza'

def get_sum(i,BITree):
    sum=0
    i+=1
    while i>0:
        sum+=BITree[i]
        i-=(i&-i)
    return sum

def update(val,n,i,BITree):
    # BITree, we see one position ahead
    i+=1
    while i<=n:
        BITree[i]+=val
        i+=(i&-i)

def construct_BIT(arr):
    n=len(arr)
    BITree=[0]*(n+1)

    for i,val in enumerate(arr):
        update(val,len(arr),i,BITree)

    return BITree

a=[1,2,3,4]
tree=construct_BIT(a)
print get_sum(2,tree)