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

        test_list2=[
            ['New York, NY', 481486, 3841],
            ['Los Angeles-Long Beach-Anaheim, CA', 674786, 15235]
            # ['Chicago, IL', 238978, 2432]
            # ['Dallas-Fort Worth, TX', 253299, 5559]
            # ['Philadelphia, PA', 248836, 7541]
        ]

        self.assertEqual(optimizeInvestments(test_list2, 1000000, 100000),(15235,['Los Angeles-Long Beach-Anaheim, CA']))
        self.assertEqual(optimizeInvestments(test_list2, 500000, 100000),(3841,['New York, NY']))
        self.assertEqual(optimizeInvestments(test_list2, 1000000, 10000),(15235,['Los Angeles-Long Beach-Anaheim, CA']))
        self.assertEqual(optimizeInvestments(test_list2, 1000000, 1000),(15235,['Los Angeles-Long Beach-Anaheim, CA']))


        test_list3=[
           # ['New York, NY', 481486, 3841],
            ['Los Angeles-Long Beach-Anaheim, CA', 674786, 15235],
            ['Chicago, IL', 238978, 2432]
            # ['Dallas-Fort Worth, TX', 253299, 5559]
            # ['Philadelphia, PA', 248836, 7541]
        ]

        self.assertEqual(optimizeInvestments(test_list3, 1000000, 100000),(15235+2432,['Chicago, IL', 'Los Angeles-Long Beach-Anaheim, CA']))

        self.assertEqual(optimizeInvestments(test_list3, 100000, 100000),(0,[]))


if __name__ == '__main__':
    unittest.main()