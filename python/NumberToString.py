
class NumToString:
    digits = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    other = ['','Thousand','Million','Billion','Trillion']

    def numToString(self,n):
        if n==0:
            return 'Zero'
        elif n<0:
            return 'Negative '+self.numToString(-1*n)

        str=''
        iter=0

        while n>0:
            cur_val = n%1000
            print cur_val
            str=self.numToString100(cur_val)+' '+self.other[iter]+' '+str
            n = n/1000
            iter+=1

        return str

    def numToString100(self,n):
        str=''
        if n>100:
            num=n/100
            n=n%100
            str=self.digits[num-1]+' Hundred'

        if 11<=n<20:
            str=str+' '+self.teens[11-n]
            return str
        elif n>=10:
            str=str+' '+self.tens[n/10-1]
            n=n%10

        if n>0:
            str=str+' '+self.digits[n-1]

        return str

A=NumToString()
print A.numToString(22025005110)