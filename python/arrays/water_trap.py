class Solution(object):
    def trap_opt1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        ans = 0
        left_max=0; right_max=0
        left=0; right=len(height)-1
        while left<=right:
            if left_max<right_max:
                # update left
                if height[left]>=left_max:
                    left_max=height[left]
                else:
                    ans+=left_max-height[left]
                left+=1
            else:
                # update right
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    ans+=right_max-height[right]
                right-=1
        return ans

    # I feel this is better
    def trap_opt2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        ans = 0
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            print left, right
            if height[left] < height[right]:
                # update left
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                # update right
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

# 2 0 2 - Input
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""