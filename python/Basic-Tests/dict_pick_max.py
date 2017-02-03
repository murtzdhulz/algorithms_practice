__author__ = 'Murtaza'

import operator

d={'a':1.4,'b':0.3,'c':9.9,'d':10.1,'e':1.5,'f':2.1,'g':5.2,'h':5.1,'i':5.3,'p':18.9}
# newA = dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
f={('a','z'):1.4,('b','r'):0.3,('c','l'):9.9,('d','s'):10.1,('e','y'):1.5,('f','x'):2.1,('g','o'):5.2,('h','u'):5.1,('i','q'):5.3,('p','t'):18.9}

newA = (sorted(f.iteritems(), key=lambda val:val[1], reverse=True)[:5])
print newA

k=[(('a','z'),1.4),(('b','r'),0.3),(('c','l'),9.9),(('d','s'),10.1)]
print sorted(k, key=lambda val:val[1], reverse=True)[:3]
