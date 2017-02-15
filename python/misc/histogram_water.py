__author__ = 'Murtaza'

def get_volume(hist):
    left_max_arr=[0]*len(hist)

    left_max=hist[0]
    for i in xrange(len(hist)):
        left_max=max(left_max,hist[i])
        left_max_arr[i]=left_max

    # doing the backward sweep along with the other calculations
    sum=0
    right_max=hist[-1]

    for i in xrange(len(hist)-1,-1,-1):
        right_max=max(hist[i],right_max)
        second_tallest=min(right_max,left_max_arr[i])
        if second_tallest>hist[i]:
            sum+=second_tallest-hist[i]

    return sum

histogram=[0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]
print "The volume is:",get_volume(histogram)
