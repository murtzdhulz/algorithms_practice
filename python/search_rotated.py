def find_element(a,k,lo,hi):
    if hi < lo:
        return -1

    mid=(hi+lo)//2

    if a[mid]==k:
        return mid

    # left half is proper
    if a[mid] > a[lo]:
        if a[lo] <= k < a[mid]:
           return find_element(a,k,lo,mid-1)
        else:
            return find_element(a,k,mid+1,hi)

    # right half is proper
    elif a[mid] < a[lo]:
        if a[mid] < k <= a[hi]:
            find_element(a,k,mid+1,hi)
        else:
            find_element(a,k,lo,mid-1)

    # same value on the left
    elif a[mid] == a[lo]:
        if a[lo] != a[hi]:
            return find_element(a,k,mid+1,hi)
        else:
            p=find_element(a,k,lo,mid-1)
            if p==-1:
                return find_element(a,k,mid+1,hi)
            else:
                return p

    else:
        # This part is not needed
        print "Entered here"
        return -1

arr=[1,2,3,7,9,10,11]
arr_rot = [7,9,10,11,1,2,3]
print find_element(arr_rot,3,0,len(arr_rot)-1)
