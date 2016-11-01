__author__ = 'Murtaza'

# in a sorted list of numbers find if a magic index exists
def magic_index_distinct(arr,start,end):
    if start>end:
        return False,None

    mid=(start+end)//2
    if arr[mid]==mid:
        return True,mid
    elif arr[mid]>mid:
        return magic_index_distinct(arr,start,mid-1)
    else:
        return magic_index_distinct(arr,mid+1,end)

l=[-40,-20,-1,1,2,3,5,7,9,12,13]
print magic_index_distinct(l,0,len(l)-1)