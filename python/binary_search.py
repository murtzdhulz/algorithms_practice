__author__ = 'Murtaza'

def binary_search_recursive(ele,arr,start,end):
    if start>end:
        return False,None

    mid=(start+end)//2
    if arr[mid] == ele:
        return True,mid
    elif arr[mid]<ele:
        return binary_search_recursive(ele,arr,mid+1,end)
    else:
        return binary_search_recursive(ele,arr,start,mid-1)

# print binary_search_recursive(2,[2],0,0)
l=sorted([210,100,7885,5,21,10,69,2])
print l,len(l)
print binary_search_recursive(21,l,0,7)