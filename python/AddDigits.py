__author__ = 'Murtaza'

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num))>1):
            num=self.get_sum(num)
        return num

    def get_sum(self, n):
        cur_sum=0
        while(n>0):
            cur_digit = n%10
            cur_sum+=cur_digit
            n/=10
            print n
        return cur_sum

ans=Solution()
print ans.addDigits(19)

