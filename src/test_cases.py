import unittest
import math
from a_m import arrayManipulation

class TestArrayManipulation(unittest.TestCase):
    
    def test_array_manipulation_basic(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expected_output = 200
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)
        
    def test_array_manipulation_empty_queries(self):
        n = 5
        queries = []
        expected_output = 0
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)
        
    def test_array_manipulation_single_query(self):
        n = 5
        queries = [[1, 5, 10]]
        expected_output = 10
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)
        
    def test_array_manipulation_all_queries_same(self):
        n = 5
        queries = [[1, 5, 10], [1, 5, 10], [1, 5, 10]]
        expected_output = 30
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)

    def test_array_manipulation_n_lower_than_b(self):
        n=4
        queries = [[1, 2, 100], [2, 5, 100], [3, 5, 100]]
        expected_output = -1
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)

    def test_array_manipulation_mutation(self):
        n = 5
        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
        expected_output = 200
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)


    def test_n_lower_bound(self):
        n = 2
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n,queries), -1)

    def test_n_upper_bound(self):
        n = int(math.pow(10,9))
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    
    def test_a_lower_than_1(self):
        n = 4
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_a_greater_than_b(self):
        n = 4
        queries = [[1,2,3],[1,1,4],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

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

    

        
    # def test_array_manipulation_large_input(self):
    #     n = math.pow(10,8)
    #     queries = [[1, 2, 100], [3, 5, 200], [2, 4, 50], [10, 12, 500]]
    #     expected_output = -1
        
    #     result = arrayManipulation(n, queries)
        
    #     self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
