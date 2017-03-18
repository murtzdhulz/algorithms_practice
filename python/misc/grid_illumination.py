__author__ = 'Murtaza'
from collections import defaultdict

class illumination:
    def __init__(self,lamps_list=None):
        self.rows=defaultdict(int)
        self.columns=defaultdict(int)
        self.d1=defaultdict(int)
        self.d2=defaultdict(int)
        self.lamps=set()

        if lamps_list:
            for l in lamps_list:
                l=tuple(l)
                self.lamps.add(l)
                self.rows[l[0]]+=1
                self.columns[l[1]]+=1
                self.d1[self.get_diagnol_1(l)]+=1
                self.d2[self.get_diagnol_2(l)]+=1
        print self.rows
        print self.columns
        print self.d1
        print self.d2
        print self.lamps
        print lamps_list

    def is_illuminated(self,query):
        print query,query[0],query[1]
        neighbors=self.get_neighbors(query)
        rc,cc,d1c,d2c=self.rows[query[0]],self.columns[query[1]],self.d1[self.get_diagnol_1(query)],self.d2[self.get_diagnol_2(query)]
        print "The counts before:",rc,cc,d1c,d2c
        for n in neighbors:
            n=tuple(n)
            if n in self.lamps:
                # one on the left or right
                if n[0]==query[0]:
                    rc-=1
                # one on the top or bottom
                if n[1]==query[1]:
                    cc-=1
                # d2
                if (n[0]+n[1])==(query[0]+query[1]):
                    d2c-=1
                if (n[0]-n[1])==(query[0]-query[1]):
                    d1c-=1
        print "The counts after:",rc,cc,d1c,d2c
        return rc!=0 or cc!=0 or d1c!=0 or d1c!=0 or d2c!=0

    def get_neighbors(self,p):
        l=[]
        for i in xrange(-1,2,1):
            for j in xrange(-1,2,1):
                l.append([p[0]+i,p[1]+j])
        return l

    # r - row index, c - column index
    def get_diagnol_1(self,p):
        return p[1]-p[0]

    def get_diagnol_2(self,p):
        return p[1]+p[0]

def brute_iiluminate(lamps,queries):
    # lamp_set=set()
    result=[]
    for q in queries:
        flag=False
        neighbors=get_neighbors(q)
        for l in lamps:
            if l in neighbors:
                print "came here:",l,neighbors
                continue
            if l[0]==q[0]:
                flag=True
                break
            if l[1]==q[1]:
                flag=True
                break
            if l[0]+l[1]==q[0]+q[1]:
                flag=True
                break
            if l[0]-l[1]==q[0]-q[1]:
                flag=True
                break
        result.append(flag)

    return result

def get_neighbors(p):
        l=[]
        for i in xrange(-1,2,1):
            for j in xrange(-1,2,1):
                l.append([p[0]+i,p[1]+j])
        return l

# o=illumination()
# print o.get_neighbors((2,1))
# lamps=[[1,1],[2,3],[4,1]]
# o=illumination(lamps)
# print
# print o.is_illuminated([4,2])

# lamps=[[1,1],[2,3],[4,1]]
# query=[[4,2],[3,3]]
# print brute_iiluminate(lamps,query)

# o=illumination()
# print o.get_neighbors((2,1))
lamps=[[4,3],[4,4]]
o=illumination(lamps)
print
print o.is_illuminated([7,6])

"""
# Complete the function below.
from collections import defaultdict

def  checkIllumination(N, lamps_list, queries):
    # do some preprocessing and populate lists for lookup
    rows=defaultdict(int)
    columns=defaultdict(int)
    d1=defaultdict(int)
    d2=defaultdict(int)
    lamps=set()
    result=[]

    if lamps_list:
        for l in lamps_list:
            l=tuple(l)
            lamps.add(l)
            rows[l[0]]+=1
            columns[l[1]]+=1
            d1[get_diagnol_1(l)]+=1
            d2[get_diagnol_2(l)]+=1

    for query in queries:
        neighbors=get_neighbors(query)
        rc,cc,d1c,d2c=rows[query[0]],columns[query[1]],d1[get_diagnol_1(query)],d2[get_diagnol_2(query)]
        for n in neighbors:
            n=tuple(n)
            if n in lamps:
                # one on the left or right
                if n[0]==query[0]:
                    rc-=1
                # one on the top or bottom
                if n[1]==query[1]:
                    cc-=1
                # d2
                if (n[0]+n[1])==(query[0]+query[1]):
                    d2c-=1
                # d1
                if (n[0]-n[1])==(query[0]-query[1]):
                    d1c-=1
        if rc!=0 or cc!=0 or d1c!=0 or d1c!=0 or d2c!=0:
            result.append("LIGHT")
        else:
            result.append("DARK")
    return result

def get_diagnol_1(p):
    return p[1]-p[0]

def get_diagnol_2(p):
    return p[1]+p[0]

def get_neighbors(p):
    l=[]
    for i in xrange(-1,2,1):
        for j in xrange(-1,2,1):
            l.append([p[0]+i,p[1]+j])
    return l
"""