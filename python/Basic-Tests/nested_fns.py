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
        def func_inner():
            some_var = 5
            visit.add(10)
        func_inner()
        print visit
        print some_var

s=Solution()
# s.a(5)
s.some_func()

# https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping (look at the second explanation)