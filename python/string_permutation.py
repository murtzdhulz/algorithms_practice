__author__ = 'Murtaza'

def string_permute1(s,start,end):
    if start==end:
        print ''.join(s)
    else:
        for i in xrange(start,end+1):
            s[start],s[i]=s[i],s[start]
            string_permute1(s,start+1,end)
            s[start],s[i]=s[i],s[start]

# n is the ending index
def string_permute2(s,n):
    if n==0:
        print ''.join(s)
    else:
        for i in xrange(n+1):
            s[i],s[n]=s[n],s[i]
            string_permute2(s,n-1)
            s[i],s[n]=s[n],s[i]

string='ABC'
string_permute1(list(string),0,len(string)-1)
print
string_permute2(list(string),len(string)-1)
