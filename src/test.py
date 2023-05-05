import unittest
import math
from a_m import arrayManipulation
#basic 200
#all same 30
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
        queries = [[1, 5, 100], [2, 5, 100], [3, 5, 100]]
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
        n = 100000001
        queries = [[1,0,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_a_lower_greater_than_1(self):
        n = 4
        queries = [[2,3,3],[3,4,5],[10,10,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_a_lower_than_1(self):
        n = 4
        queries = [[0,0,3],[3,4,5],[10,10,10]]
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
        queries = [[1,1,3],[1,2,4],[10,3,10]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_b_lower_than_n_v2(self):
        n = 5
        queries = [(1, 3, 10), (4, 6, 5)]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_lower_bound(self):
        n = 4
        queries = [[1,2,-1],[3,4,5],[0,10,10]]
    
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_k_upper_bound(self):
        n = 4
        queries = [[1,2,2000],[3,4,2000],[10,10,2000]]
        self.assertEqual(arrayManipulation(n, queries), -1)

    def test_or_into_and(self):
        n = 5
        queries = [(1, 2, 5), (2, 4, 10), (0, -1, 15)]
        assert arrayManipulation(n, queries) == -1
        
        
    def test_array_manipulation_large_input(self):
        n = int(math.pow(10,8))
        queries = [[1, 2, 100], [3, 5, 200], [2, 4, 50], [10, 12, 500]]
        expected_output = -1
        
        result = arrayManipulation(n, queries)
        
        self.assertEqual(result, expected_output)

        ########################################################################
        ##########################################################
    def test_case_3(self):
        n = 4
        queries = [[2,3,603],[1,1,286],[4,4,882]]
        self.assertEqual(arrayManipulation(n, queries), 882)

    def test_case_4(self):
        n = 3
        queries = [[1,2,100],[2,3,100],[1,3,100]]
        self.assertEqual(arrayManipulation(n, queries), 300)



if __name__ == '__main__':
    unittest.main()
