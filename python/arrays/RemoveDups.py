# Remove duplicates from an array in place

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0

        i=0
        j=1

        while j<len(nums):
            if nums[j-1]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                j+=1
        print nums
        return i+1

k=[1,1,2]
l=[1,1,5,5,5,5,5,5,7,9,10,11,11,11,13]
print removeDuplicates(l)
