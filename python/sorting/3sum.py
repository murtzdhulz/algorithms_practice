__author__ = 'Murtaza'

def three_sum(arr):
    res=[]

    # we first sort the numbers
    arr.sort()
    # print "Sorted numbers:",arr

    for i in range(len(arr)-2):
        # If the first value itself is positive, you will never get a sum = 0 with anything else you see later
        if arr[i]>0:
            break
        if i>0 and arr[i]==arr[i-1]:
            # print "Continuing with:",arr[i],i
            continue
        j,k=i+1,len(arr)-1

        while j<k:
            sum=arr[i]+arr[j]+arr[k]
            if sum<0:
                # need to move j
                while j<k and arr[j]==arr[j+1]:    # Skip duplicates
                    j+=1
                j+=1
            elif sum>0:
                # need to move k
                while j<k and arr[k]==arr[k-1]:
                    k-=1
                k-=1
            else:
                res.append([arr[i],arr[j],arr[k]])
                while j<k and arr[j]==arr[j+1]:    # Skip duplicates
                        j+=1
                while j<k and arr[k]==arr[k-1]:
                    k-=1
                j+=1
                k-=1
    return res

# nums=[-1,0,1,2,-1,-4]

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]   # Failed initially
# Expected output: [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
print three_sum(nums)
