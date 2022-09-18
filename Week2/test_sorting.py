
import unittest
from lab2_sorting import *
import numpy as np
import random

class TestMatrixMult(unittest.TestCase):

    def test_dot(self):
        n=10
        A = [i for i in range(n)]
        random.shuffle(A)
        self.assertEqual([0,1,2,3,4,5,6,7,8,9], insertionSort(A))
        self.assertEqual([0,1,2,3,4,5,6,7,8,9], mergeSort(A))
        self.assertEqual([0,1,2,3,4,5,6,7,8,9], bubbleSort(A))
        num_tests = 10000
        for i in range(num_tests):
            list_len = np.random.randint(1, 100)
            A = [i for i in range(list_len)]
            random.shuffle(A)
            insertion_sorted = insertionSort(A)
            merge_sorted = mergeSort(A)
            bubble_sorted = bubbleSort(A)
            A.sort()
            self.assertEqual(A, insertion_sorted)
            self.assertEqual(A, merge_sorted)
            self.assertEqual(A, bubble_sorted)



if __name__ == '__main__':
    unittest.main()