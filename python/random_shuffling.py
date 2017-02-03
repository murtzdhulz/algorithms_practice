__author__ = 'Murtaza'
import random

def random_shuffling(size):
    l = range(size)

    print "Before shuffling:",l

    for i in range(size):
        rand = 0+int(random.random()*(i-0+1))     # lower+int(random*(heigher-lower+1))

        # print "Moving index %d to index %d" %(rand,i)
        # swap rand index with i
        l[i],l[rand] = l[rand],l[i]

    print "After shuffling:",l

random_shuffling(50)