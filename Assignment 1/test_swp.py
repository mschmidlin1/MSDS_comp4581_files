#from doctest import testfile
import unittest
from swp import *
#import numpy as np

class TestMatrixMult(unittest.TestCase):

    def test_unique_tuples(self):
        self.assertEqual(set([1,2,3,4,5]), unique_tuples([(1, 2), (1,3), (4, 5), (3, 2), (5, 2), (5, 1)]))

    def test_queue(self):
        Q = MyQueue()
        Q.enqueue(1)
        Q.enqueue(2)
        self.assertEqual([1,2], Q.queue)
        Q.dequeue()
        self.assertEqual([2], Q.queue)
        self.assertFalse(Q.empty())
        Q.dequeue()
        self.assertTrue(Q.empty)
        self.assertEqual([], Q.queue)

    def test_BFS(self):
        G = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
        s = "A"
        self.assertEqual([("A", 0), ("B", 1), ("C", 1)], BFS(G, s))

        G = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B", "D"], "D": ["C"]}
        s = "A"
        self.assertEqual([("A", 0), ("B", 1), ("C", 1), ("D", 2)], BFS(G, s))

        s = "D"
        self.assertEqual([("A", 2), ("B", 2), ("C", 1), ("D", 0)], BFS(G, s))

        s = "C"
        self.assertEqual([("A", 1), ("B", 1), ("C", 0), ("D", 1)], BFS(G, s))

    def test_distancedist(self):
        G = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B", "D"], "D": ["C"]}
        self.assertEqual({0: 25.0, 1: 50.0, 2: 25.0}, distanceDistribution(G))

if __name__ == '__main__':
    unittest.main()