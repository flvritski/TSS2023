import math
import unittest
from a_m import arrayManipulation

class boundaryValueAnalaysis(unittest.TestCase):

    def test_n_lower_bound(self):
        n = 2
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_n_upper_bound(self):
        n = math.pow(10,9)
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    
    def test_a_lower_than_1(self):
        n = 4
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_a_greater_than_b(self):
        n = 4
        queries = [[1,2,3],[1,1,4],[10,10,10]]
        
        self.assertEqual(arrayManipulation(n,queries), -1)

    def test_b_lower_than_a(self):
        n = 4
        queries = [[1,2,3],[1,1,4],[10,10,10]]
    
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_b_lower_than_n(self):
        n = 4
        queries = [[1,2,3],[1,5,4],[10,10,10]]
       
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_lower_bound(self):
        n = 4
        queries = [[1,2,3],[3,4,5],[0,10,10]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_upper_bound(self):
        n = 4
        queries = [[1,2,3],[3,4,5],[10,10,math.pow(10,9)]]

        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_solution(self):
        n = 4
        queries = [[1,2,3],[3,4,5],[10,10,10]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    
    
    # ======= n=math.pow(10,7) ========
    
    
    def test_a_lower_than_1_n_max(self):
        n = int(math.pow(10,8))
        queries = [[1,0,3],[3,4,5],[10,10,10]]

        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_a_greater_than_n_max_b(self):
        n = int(math.pow(10,8))
        queries = [[1,2,3],[1,1,4],[10,10,10]]

        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_b_lower_than_a_n_max(self):
        n = int(math.pow(10,8))
        queries=[[1,2,3],[1,1,4],[10,10,10]]

        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_b_lower_than_n_n_max(self):
        n = int(math.pow(10,8))
        queries = [[1,2,3],[1,5,4],[10,10,10]]
       
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_lower_bound_n_max(self):
        n = int(math.pow(10,8))
        queries = [[1,2,3],[3,4,5],[0,10,10]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_upper_bound_n_max(self):
        n = int(math.pow(10,8))
        queries = [[1,2,3],[3,4,5],[10,10,int(math.pow(10,9))]]
        
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_solution_n_max(self):
        n = int(math.pow(10,7))
        queries = [[1,2,3],[3,4,5],[10,10,10]]
       
        self.assertEqual(arrayManipulation(n, queries), 10)
    
    def test_array_manipulation_boundary(self):
        # test case with minimum input values
        n = 1
        queries = [[1, 1, 1]]
        expected_output = -1
        self.assertEqual(arrayManipulation(n, queries), expected_output)
        
        # test case with maximum input values
        n = 10**7
        queries = [[1, n, 10], [n, n, 10], [1, 1, 10], [n//2, n//2+1, 10]]
        expected_output = 20
        self.assertEqual(arrayManipulation(n, queries), expected_output)
        
        # test case with a large number of queries
        n = 5
        queries = [[1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]] * 10**4
        expected_output = 20000
        self.assertEqual(arrayManipulation(n, queries), expected_output)


    # def test_a_greater_than_b(self):
    #     n = 5
    #     a = [3, 1, 4, 2, 5]
    #     b = [2, 3, 5, 4, 5]
    #     k = [10, 20, 30, 40, 50]
    #     with self.assertRaises(ValueError):
    #         arrayManipulation(n, a, b, k)

if __name__ == '__main__':
    unittest.main()
