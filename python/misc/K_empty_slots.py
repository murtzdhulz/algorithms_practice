__author__ = 'Murtaza'

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days=[None]*(len(flowers))
        # Make the days array such that days[i] is the blooming day of flower in position i+1
        for i in xrange(len(flowers)):
            days[flowers[i]-1] = i+1

        left = 0
        right = k+1
        res = float('inf')
        for i in xrange(len(flowers)):
            if right>=len(flowers):
                break
            if (days[i]<days[left] or days[i]<=days[right]):
                if (i==right):
                    # We have found the subarray
                    res = min(res, max(days[right], days[left]))
                left = i
                right = i+k+1
        return res if res!=float('inf') else -1

"""
Question:
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.
"""