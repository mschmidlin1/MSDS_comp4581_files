
import unittest
from schmidlin_lab6 import *

class TestMatrixMult(unittest.TestCase):

    def test_mystack(self):
        self.assertEqual(1,1)


        s = MyHashtable(10)

        self.assertEqual(10, s.size)
        self.assertFalse(s.member('amy'))
        s.insert("amy") #97
        self.assertTrue(s.member('amy'))
        self.assertEqual('amy', s.table[7])
        self.assertEqual('filled', s.status[7])
        self.assertEqual('empty', s.status[1])
        self.assertEqual(None, s.table[1])
        s.insert("chase") #99
        self.assertTrue(s.member('chase'))
        self.assertEqual('filled', s.status[9])
        self.assertEqual('chase', s.table[9])
        s.insert("chris") #99
        self.assertTrue(s.member('chris'))
        self.assertEqual('chris', s.table[0])
        self.assertEqual('filled', s.status[0] )
        s.delete("chase")
        self.assertEqual('deleted', s.status[9])
        self.assertEqual(None, s.table[9])
        self.assertFalse(s.member('chase'))





if __name__ == '__main__':
    unittest.main()