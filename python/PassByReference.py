__author__ = 'Murtaza'

class FunctionCheck:
    def func1(self,a):
        print 'Before function call',a
        b=self.func2(a)
        print 'After function call',a
        return b

    def func2(self,l):
        l[2]=5
        b=[2,2,2]
        return b

ans=FunctionCheck()
print ans.func1([100,200,500])
