__author__ = 'Murtaza'
from stack import Stack

def sort_stack(s):
    buffer = Stack()

    while(not s.is_empty()):
        k = s.pop()
        # print "Value of k is:",k
        while not buffer.is_empty() and k < buffer.peek():
            s.push(buffer.pop())
        # print "Pushing k:",k
        buffer.push(k)

    while not buffer.is_empty(): s.push(buffer.pop())

def print_stack(s):
    print s.items[::-1]

s=Stack()
s.push(5)
s.push(100)
s.push(8)
s.push(12)
s.push(10)
s.push(1)
s.push(321)
s.push(52)
s.push(51)
s.push(53)

print_stack(s)

sort_stack(s)

print_stack(s)