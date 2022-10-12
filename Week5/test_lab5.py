
import unittest
from schmidlin_lab5 import *

class TestMatrixMult(unittest.TestCase):

    def test_mystack(self):
        s = MyStack()
        self.assertTrue(s.empty())
        s.push(5)
        self.assertEqual(5, s.top())
        s.push(8)
        self.assertEqual(8, s.top())
        self.assertEqual(8, s.pop())
        self.assertEqual(5, s.top())
        self.assertFalse(s.empty())
        self.assertEqual(5, s.pop())
        self.assertTrue(s.empty())

        with self.assertRaises(IndexError) as context:
            s.pop()
    
    def test_myqueue(self):
        q = MyQueue()
        self.assertTrue(q.empty())
        q.enqueue(5)
        self.assertEqual(5, q.front())
        self.assertFalse(q.empty())
        q.enqueue(8)
        self.assertEqual(5, q.front())
        self.assertEqual(5, q.dequeue())
        q.enqueue(3)
        self.assertEqual(8, q.front())
        self.assertEqual(8, q.dequeue())
        self.assertFalse(q.empty())
        self.assertEqual(3, q.dequeue())
        self.assertTrue(q.empty())

        with self.assertRaises(IndexError) as context:
            q.dequeue()






if __name__ == '__main__':
    unittest.main()