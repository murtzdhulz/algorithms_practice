__author__ = 'Murtaza'

def subsets(p):
   n=len(p)
   i=0
   while i<(1<<n):
       # print bin(i)
       cur_set='{'
       for j in range(n):
           if (i & (1<<j)) > 0:
               # print p[j]
               cur_set=cur_set+p[j]+','
       cur_set=cur_set.rstrip(',')+'}'
       print cur_set
       i+=1

subsets(['a','b','c','d','e'])