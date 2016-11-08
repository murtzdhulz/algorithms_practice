def a():
    print "I am inside A"

class B:
    def Yo(self):
        a()

ob=B()
ob.Yo()