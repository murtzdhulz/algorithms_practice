__author__ = 'Murtaza'

class CheckPalindrome:
    def isPalindromPermutation(self, str):
        oddcount = 0
        table=[0]*128
        for c in str:
            index = ord(c) - ord('A')
            print 'index is:',c,index
            table[index]+=1
            if table[index]%2 == 1:
                oddcount+=1
            else:
                oddcount-=1
        return oddcount<=1

o = CheckPalindrome()
print o.isPalindromPermutation('aaabbAA')