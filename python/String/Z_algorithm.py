__author__ = 'Murtaza'

def get_Z_array(s):
    n=len(s)
    z_arr=[0]*len(s)
    z_arr[0]=len(s)
    l=r=k=0

    # We will maintain [L R] interval
    for i in range(1,n):
        if i>r:
            # Readjust L and R
            l=r=i
            while r<n and s[r]==s[r-l]:
                r+=1
            z_arr[i]=r-l
            r-=1

        else:
            k=i-l

            if z_arr[k]<r-l+1:
                z_arr[i]=z_arr[k]   # There is no new substring from i which would be of greater length than one given by Z[k]
            else:
                l=i
                while r<n and s[r]==s[r-l]:
                    r+=1
                z_arr[i]=r-l
                r-=1
    return z_arr

def search(pattern,T):
    concat=pattern+"$"+T
    z=get_Z_array(concat)

    for i in range(len(concat)):
        if z[i]==len(pattern):
            print "Match found at position:",i-len(pattern)-1

search('aba','kabaababbcaba')

