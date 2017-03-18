__author__ = 'Murtaza'

def max_sum_subarray(nums):
    # table to store the sum of a particular subarray
    # in line if T[i-1]<0:, if we use "<=" instead, the number of elements in the subarray will be lesser
    T=[0]*len(nums)
    T[0]=nums[0]
    max_sum=nums[0]
    max_start=0
    max_end=1
    cur_start=0
    cur_end=1
    for i in range(1,len(nums)):
        # then start a new ssubarray from here
        if T[i-1]<=0:
            cur_start=i
            cur_end=i+1
            T[i]=nums[i]
        else:
            cur_end+=1
            T[i]=nums[i]+T[i-1]
        if max_sum<T[i]:
            max_sum=T[i]
            max_start=cur_start
            max_end=cur_end
    return max_sum,nums[max_start:max_end],max_start,max_end

def max_sum_subarray_2(nums):
    cur_sum=max_sum=nums[0]
    for val in nums[1:]:
        cur_sum=max(val,cur_sum+val)
        max_sum=max(max_sum,cur_sum)
    return max_sum

a=[-2,1,-3,4,-1,2,1,-5,4]
b=[-5,5,0,-5,0,5,0]
print max_sum_subarray(b)

print max_sum_subarray_2(a)