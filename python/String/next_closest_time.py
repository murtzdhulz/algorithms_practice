__author__ = 'Murtaza'
import itertools

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        start_time = next_closest = 60*(int(time[:2]))+(int(time[3:]))
        max_time = 60*24

        digits = [int(x) for x in time if x!=":"]

        for h1,h2,m1,m2 in itertools.product(digits,repeat=4):
            cur_hrs = h1*10+h2
            cur_mins = m1*10+m2
            if cur_hrs<24 and cur_mins<60:
                # Then this time can be displayed
                cur_time = cur_hrs*60+cur_mins
                time_elapsed = (cur_time-start_time)%(24*60)
                if 0<time_elapsed<max_time:
                    max_time = time_elapsed
                    next_closest = cur_time
        return "{:02d}:{:02d}".format(*divmod(next_closest,60))