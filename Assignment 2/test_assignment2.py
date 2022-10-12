#from doctest import testfile
import unittest
from schmidlin_assignment2 import *


def MaxProfit(A):
    """Given a list A of stock prices, find the buy and sell times that maximize profit"""
    best,buy,sell = 0,0,0
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            profit = A[j]-A[i]
            if profit > best:
                best,buy,sell = profit,i,j
    best = round(best, 6)
    if best<=0:
        return 0,0,0
    return buy,sell,best


class TestMatrixMult(unittest.TestCase):

    def test_price_to_changes(self):
        self.assertEqual([-2,5,1], list(prices_to_changes([4,2,7,8])))

        self.assertEqual([17,-10,-4,-3,1], list(prices_to_changes([-8,  9, -1, -5, -8, -7])))

    def test_maxProfit(self):

        self.assertEqual((1,2,8), maxProfit([ 4,  1,  9,  4,  0, -4]))
        self.assertEqual((2,3,6), maxProfit([ -7,  -2, -10,  -4]))
        self.assertEqual((0,3,3), maxProfit([1,2,3,4]))
        self.assertEqual((0,0,0), maxProfit([0,0,0,0]))
        self.assertEqual((0,0,0), maxProfit([4,3,2,1]))
        self.assertEqual((0,0,0), maxProfit([0,0,0,0]))
        self.assertEqual((5,6,17), maxProfit([ 7,  5,  2, -8,  3, -9,  8, -7,  7, -5]))
        self.assertEqual((0,4,4), maxProfit([ 1, 2, 3, 4, 5, 4, 3, 2, 1]))
        self.assertEqual((4,8,4), maxProfit([ 5,4,3,2,1,2,3,4,5]))
        self.assertEqual((0,1,20.8), maxProfit([ 0.0, 20.8, 0.0]))
        self.assertEqual((0,1,20.8), maxProfit([ 0, 20.8, 4]))

        self.assertEqual((8, 11, 173.115059), maxProfit([
            -52.74517971, -48.74852634, -52.01308522, -85.91403649, -21.18429956, 
            -11.74721857, -68.58562717,  48.1886253,  -94.50649675,  13.88715425,
            -68.43356516,  78.60856217, -90.33471776,  17.87781784,  47.26206383,
            27.02750836, -21.05281523,  14.73757495,  45.09051185]))

        self.assertEqual((0, 0, 0), maxProfit([ 61.89146256, -65.3761185 ]))



        num_tests = 10000
        for i in range(num_tests):
            arr_length = np.random.randint(low=1, high=10)
            prices = np.random.uniform(low=-100, high=100, size=arr_length)
            #print(f"Arr Length: {arr_length}")
            #[print(price, end=',') for price in prices]
            truth = MaxProfit(prices)
            myanswer = maxProfit(prices)
            if truth!=myanswer:
                print(prices)
                print(f"Truth: {truth}")
                print(f"My Answer: {myanswer}")
                exit()
            self.assertEqual(truth, myanswer)





if __name__ == '__main__':
    unittest.main()