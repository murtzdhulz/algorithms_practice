class Solution:
    def a(self,p):
        l=0
        def b(k):
            if l==5:
                print "Hi"

        l = p
        b(7)
        print l

    def some_func(self):
        visit=set()
        some_var = 0
        lps=[0]*5
        s="PORT"
        def func_inner():
            some_var = 5
            visit.add(10)
            lps[2]=100
            s="NEW"
        func_inner()
        print visit
        print some_var
        print lps
        print s

    def new_fn(self):
        def b():
            print l
        l=[1,2,3]
        b()


s=Solution()
# s.a(5)
# s.some_func()
s.new_fn()

# https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping (look at the second explanation)