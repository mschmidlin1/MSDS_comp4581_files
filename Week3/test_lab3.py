
import unittest
from schmidlin_lab3 import *
import numpy as np
import random

class TestMatrixMult(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(11))
        self.assertTrue(isPrime(13))
        self.assertTrue(isPrime(97))

        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(20))
        self.assertFalse(isPrime(100))
        self.assertFalse(isPrime(1000))
        self.assertFalse(isPrime(675))

    def test_factor(self):
        p = nBitPrime(10)
        q = nBitPrime(10)
        self.assertEqual(set([p,q]), factor(p*q))

        p = nBitPrime(12)
        q = nBitPrime(12)
        self.assertEqual(set([p,q]), factor(p*q))

        p = nBitPrime(5)
        q = nBitPrime(5)
        self.assertEqual(set([p,q]), factor(p*q))

if __name__ == '__main__':
    unittest.main()