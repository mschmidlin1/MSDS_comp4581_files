

from collections import deque


class MyQueue(deque):
    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
    def dequeue(self):
        return self.queue.pop(0)
    def empty(self):
        return not bool(len(self.queue))
