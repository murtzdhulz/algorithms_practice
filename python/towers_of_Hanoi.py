__author__ = 'Murtaza'

def move_tower(h,source,dest,buffer):
    if h>=1:
        move_tower(h-1,source,buffer,dest)
        print "Move disk {} from {} to {}".format(h,source,dest)
        move_tower(h-1,buffer,dest,source)

move_tower(3,"A","B","C")