class Solution(object):
    def __init__(self):
        self.dp = {0: 0}

    def racecar(self, target):
        """
        :type target: int
        :rtype: int

        Explanation:
        Consider two general cases for number i with bit_length n.

        i==2^n-1, this case, n is the best way

        2^(n-1)-1<i<2^n-1, there are two ways to arrive at i:
        Use n A to arrive at 2^n-1 first, then use R to change the direction, by here there are n+1 operations (n A and one R),
        then the remaining is same as dp[2^n-1-i]

        Use n-1 A to arrive at 2^(n-1)-1 first, then R to change the direction, use m A to go backward,
        then use R to change the direction again to move forward, by here there are n-1+2+m=n+m+1 operations (n-1 A, two R, m A),
        current position is 2^(n-1)-1-(2^m-1)=2^(n-1)-2^m, the remaining operations is same as dp[i-(2^(n-1)-1)+(2^m-1)]=dp[i-2^(n-1)+2^m)].
        """
        if target in self.dp: return self.dp[target]
        n = target.bit_length()
        # If we take n A instructions - we move by 2**n-1 (sum of GP)
        if 2 ** n - 1 == target:
            self.dp[target] = n
        else:
            # There are two cases
            # First go ahead and then turn back - (n+1) because you did n As and 1 to turn around (R)
            self.dp[target] = self.racecar(2 ** n - 1 - target) + n + 1

            # Stop before the target, then turn around, do m As and then turn back and do more As
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target], self.racecar(target - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[target]

"""
Question:
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
"""

