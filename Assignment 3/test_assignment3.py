import unittest
from portfolio import *



class TestASS3(unittest.TestCase):

    def test_price_to_changes(self):

        test_list=[
            ['Rio Grande City, TX', 59179, 868],
            ['Freeport, IL', 64103, 2138],
            ['Pine Bluff, AR', 64234, 2333],
            ['Roanoke Rapids, NC', 67185, 985],
            ['Danville, IL', 68060, 1371]
        ]

        self.assertEqual(optimizeInvestments(test_list, 1000000, 100000),(868+2138+2333+985+1371,['Danville, IL','Roanoke Rapids, NC','Pine Bluff, AR', 'Freeport, IL', 'Rio Grande City, TX']))




if __name__ == '__main__':
    unittest.main()