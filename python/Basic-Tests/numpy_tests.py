__author__ = 'Murtaza'

import numpy as np

def tile():
    a=np.array([1,1,1]).reshape((1,3))
    b=np.array([3,3,3]).reshape((3,1))
    print a
    print b
    print a+b

tile()