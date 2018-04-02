class PowerSet:
    def powerSet1(self,set):
        result = [[]]
        for x in set:
            print 'For x=',x,[subset + [x] for subset in result]
            result.extend([subset + [x] for subset in result])
        return result

    def powerSet2(self,set):
        # find 2^n
        result=[]
        k=1<<len(set)
        for i in range(k):
            cur_set=self.intToSet(set,i)
            result.append(cur_set)
        return result

    def intToSet(self,set,k):
        cur_set=[]
        for i in range(len(set)):
            if k & 1<<i:
                cur_set.append(set[i])
        return cur_set


ans = PowerSet()
print ans.powerSet1([1,2,3])
# print ans.powerSet2([1,2,3])
# print ans.powerSet1(['a','b','c','d'])

