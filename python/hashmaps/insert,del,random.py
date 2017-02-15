__author__ = 'Murtaza'
from random import randint

class randmomized_set():
    index_map={} # maps from value to index
    value_map={} # maps from index to value
    count=0

    def insert(self,value):
        if value in self.index_map:
            return False
        self.index_map[value]=self.count
        self.value_map[self.count]=value
        self.count=len(self.index_map)

    def remove(self,value):
        if value not in self.index_map:
            return False

        index=self.index_map[value]
        if index!=self.count-1:
            new_val=self.value_map[self.count-1]
            self.value_map[index]=new_val
            self.index_map[new_val]=index
        del self.index_map[value]
        del self.value_map[self.count-1]
        self.count=len(self.index_map)
        return True

    def get_random(self):
        return self.value_map[randint(0,self.count-1)]

    # Just some random thoughts
    # def increment_count(self,v):
    #     self.count+=v
    #     return self.count

o=randmomized_set()
o.insert(55)
o.insert(11)
o.insert(99)
print o.index_map
print o.value_map
print
o.remove(55)
print o.index_map
print o.value_map
print
o.remove(11)
print o.index_map
print o.value_map
print
print o.get_random()
