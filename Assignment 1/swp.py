def loadGraph(edgeFilename):
    """
    
    """

    pass


def BFS(G, s):
    myqueue = MyQueue()

    myqueue.enqueue(s)
    
    while not myqueue.empty():
        


class MyQueue():
    def __init__(self):
        queue = {}

    def enqueue(self, e):
        self.queue.add(e)
    def dequeue(self):
        pass
    def empty(self):
        return not bool(len(self.queue))