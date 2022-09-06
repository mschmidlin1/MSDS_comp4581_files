import unittest
from lab1_matrix_multiplication import *

class TestMatrixMult(unittest.TestCase):

    def test_dot(self):
        self.assertEqual(3454, dot((1,2,3,4,5,6), (45, 75, 46 , 67, 567, 3)))
        self.assertEqual(3088, dot((1,2,-3,-4,5,6), (-45, 75, 46 , -67, 567, 3)))
        
        with self.assertRaises(TypeError) as context:
            dot([1],[2, 3])
            self.assertTrue('Cannot do dot of arrays of different length.' in context.exception)





    def test_matMult(self):
        pass
        # # Test1
        # A = [[ 2, -3, 3],
        # [-2, 6, 5],
        # [ 4, 7, 8]]
        # B = [[-1, 9, 1],
        # [ 0, 6, 5],
        # [ 3, 4, 7]]
        # C = matrixMult(A, B)
        # if not C == None:
        #     printMatrix(C)



        # # Test2
        # A = [[ 2, -3, 3, 0],
        # [-2, 6, 5, 1],
        # [ 4, 7, 8, 2]]
        # B = [[-1, 9, 1],
        # [ 0, 6, 5],
        # [ 3, 4, 7]]
        # C = matrixMult(A, B)
        # if not C == None:
        #     printMatrix(C)



        # # Test3
        # A = [[ 2, -3, 3, 5],
        # [-2, 6, 5, -2]]
        # B = [[-1, 9, 1],
        # [ 0, 6, 5],
        # [ 3, 4, 7],
        # [ 1, 2, 3]]
        # C = matrixMult(A, B)
        # if not C == None:
        #     printMatrix(C)








if __name__ == '__main__':
    unittest.main()