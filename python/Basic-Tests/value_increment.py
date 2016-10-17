p=20

def a(k):
    global p
    print p,k
    p+=1
    while k!=5:
        k+=1
        a(k)

# a(0)
# print p

def b(p):
    p+=5
    print 'Inside',p

p+=1
print 'Outside',p
b(0)