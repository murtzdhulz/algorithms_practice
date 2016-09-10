class add_one:
    def add_one(self, A):
        carry=1
        digits=[]
        n=len(A)
        A.reverse()
        # print 'reversed list is:',A
        for i in range(n):
            sum = A[i]+carry
            digits.append(sum%10)
            carry=sum/10
        if carry:
            digits.append(carry)

        A.reverse()
        digits.reverse()

        if not digits[0]:
            for i in range(n-1):
                if not digits[0]:
                    digits=digits[1:]

        return digits

num = add_one()
print num.add_one([0,1,2,3])
print num.add_one([9,9,9])
print num.add_one([0,0,0,0,0,0])