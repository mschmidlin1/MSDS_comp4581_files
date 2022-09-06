from doctest import testfile
import unittest
from lab1_matrix_multiplication import *
import numpy as np

class TestMatrixMult(unittest.TestCase):

    def test_dot(self):
        self.assertEqual(3454, dot((1,2,3,4,5,6), (45, 75, 46 , 67, 567, 3)))
        self.assertEqual(3088, dot((1,2,-3,-4,5,6), (-45, 75, 46 , -67, 567, 3)))
        
        with self.assertRaises(TypeError) as context:
            dot([1],[2, 3])
            self.assertTrue('Cannot do dot of arrays of different length.' in context.exception)

    def test_row_column(self):
        self.assertEqual([1, 2, 3, 4], row([[4, 6, 1, 6], [34, 72, 465, 7], [1, 2, 3, 4]], 2))
        self.assertEqual([34, 72, 465, 7], row([[4, 6, 1, 6], [34, 72, 465, 7], [1, 2, 3, 4]], 1))

        self.assertEqual([4, 34, 1], column([[4, 6, 1, 6], [34, 72, 465, 7], [1, 2, 3, 4]], 0))
        self.assertEqual([6, 7, 4], column([[4, 6, 1, 6], [34, 72, 465, 7], [1, 2, 3, 4]], 3))

    def test_matMult(self):

        # Test1
        A = [
            [ 2, -3, 3],
            [-2, 6, 5],
            [ 4, 7, 8]
            ]

        B = [
            [-1, 9, 1],
            [ 0, 6, 5],
            [ 3, 4, 7]]

        C = matrixMult(A, B)

        self.assertEqual([
            [7, 12, 8],
            [17, 38, 63],
            [20, 110, 95]
        ], C)

        if not C == None:
            printMatrix(C)



        # # Test2
        A = [[ 2, -3, 3, 0],
        [-2, 6, 5, 1],
        [ 4, 7, 8, 2]]
        B = [[-1, 9, 1],
        [ 0, 6, 5],
        [ 3, 4, 7]]
        C = matrixMult(A, B)
        self.assertEqual(None, C)
        if not C == None:
            printMatrix(C)



        # # Test3
        A = [[ 2, -3, 3, 5],
        [-2, 6, 5, -2]]
        B = [[-1, 9, 1],
        [ 0, 6, 5],
        [ 3, 4, 7],
        [ 1, 2, 3]]
        C = matrixMult(A, B)

        self.assertEqual([
            [12, 22, 23],
            [15, 34, 57]
        ], C)
        if not C == None:
            printMatrix(C)

    def just_Better_Testing(self):


        num_tests = 100
        for i in range(num_tests):

            outer_dim1 = np.random.randint(1, 100)
            outer_dim2 = np.random.randint(1, 100)
            inner_dim = np.random.randint(1, 100)


            A = np.random.randint(low=-100, high=100, size=(outer_dim1, inner_dim))
            B = np.random.randint(low=-100, high=100, size=(inner_dim, outer_dim2))

            testC = matrixMult(A, B)
            actualC = np.matmul(A, B)
            self.assertEqual(actualC, testC)




if __name__ == '__main__':
    unittest.main()