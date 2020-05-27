"""queue.py: A program that implements a queue."""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"


class Queue:

    # initializer
    def __init__(self):
        self._data = []


    # add element to back of queue
    def enqueue(self, element):
        self._data.append(element)


    # remove and return element from front of queue
    def dequeue(self):
        assert self.size() > 0
        return self._data.pop(0)


    # returns the number of elements waiting in the queue
    def size(self):
        return len(self._data)


    # returns the frontmost element in the queue
    def peek(self):
        return self._data[0]


    # empty the list of the queue
    def empty(self):
        self._data = []


