__author__ = 'Murtaza'

# This lambda function will basically return the key having the max count value. The input to the function should be a dictionary
argmax = lambda x : max(x.iteritems(),key=lambda y : y[1])[0]

l={'a':10,'b':11,'c':100,'d':9,'e':7}

l2={'a':"TOM",'b':"You",'c':"Long",'d':"Hey",'e':"you"}  # Has been put just for reference

for item in l.iteritems():
    print item

print argmax(l)