__author__ = 'Murtaza'

def three_sum_smaller(nums,target):
    count=0

    nums.sort()

    for i in range(len(nums)-2):
        j=i+1
        k=len(nums)-1
        while j<k:
            if nums[i]+nums[j]+nums[k]<target:
                count+=k-j
                j+=1
            else:
                k-=1
    return count

print three_sum_smaller([0, 1, 3, -2],2)