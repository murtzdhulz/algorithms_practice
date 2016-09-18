class Solution:
    def highestPossible(self,n):
        digits=[]
        while n>0:
            digits.insert(0,n%10)
            n/=10
        max=float('-inf')
        for i in range(len(digits)):
            cur_num=digits[:i]+digits[i+1:]
            cur_num=map(str,cur_num)
            cur_num=int(''.join(cur_num))
            print cur_num
            if cur_num>max:
                max=cur_num
        return max

ans = Solution()
res = ans.highestPossible(99712)
print 'Answer is:',res