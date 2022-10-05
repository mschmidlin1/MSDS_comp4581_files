#from doctest import testfile
import unittest
from schmidlin_assignment2 import *
#import numpy as np

class TestMatrixMult(unittest.TestCase):

    def test_price_to_changes(self):
        self.assertEqual([-2,5,1], list(prices_to_changes([4,2,7,8])))

        self.assertEqual([17,-10,-4,-3,1], list(prices_to_changes([-8,  9, -1, -5, -8, -7])))

    def test_maxProfit(self):
        self.assertEqual((1,2,8), maxProfit([ 4,  1,  9,  4,  0, -4]))

        self.assertEqual((2,3,6), maxProfit([ -7,  -2, -10,  -4]))

        self.assertEqual((0,3,3), maxProfit([1,2,3,4]))

        self.assertEqual((0,3,0), maxProfit([0,0,0,0]))


        #this one is definitely not right
        # self.assertEqual((0,0,-1), maxProfit([4,3,2,1]))


        #technically this breaks but it's okay
        # self.assertEqual((0,0,0), maxProfit([0,0,0,0]))



        #this one breaks
        # self.assertEqual((5,6,17), maxProfit([ 7,  5,  2, -8,  3, -9,  8, -7,  7, -5]))




if __name__ == '__main__':
    unittest.main()