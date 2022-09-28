

import unittest
from schmidlin_lab4 import *
import numpy as np
import random

class TestMatrixMult(unittest.TestCase):

    def test_cpairdist(self):
        self.assertTrue(True)
        l1 = [7, 4, 12, 14, 2, 10, 16, 6]
        my_dist = cPairDist(l1)
        self.assertEqual(1, my_dist)

        l2 = [7, 4, 12, 14, 2, 10, 16, 5]
        self.assertEqual(1, cPairDist(l2))

        l3 = [14, 8, 2, 6, 3, 10, 12]
        self.assertEqual(1, cPairDist(l3))

        l4 = [17, 83, 32, 70, 8, 15, 57, 37, 4, 75]
        self.assertEqual(2, cPairDist(l4))

        l5 = [1, 2, 2, 3]
        self.assertEqual(0, cPairDist(l5))

if __name__ == '__main__':
    unittest.main()


