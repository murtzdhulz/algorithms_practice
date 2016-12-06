__author__ = 'Murtaza'

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,v):
        self.items.append(v)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

# s=Stack()
# s.push(5)
# # s.push(9)
# # s.push(100)
# # print s.pop()
# print s.pop()
# print s.is_empty()