__author__ = 'Murtaza'

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next