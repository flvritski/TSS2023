import math
import unittest

def arrayManipulation(n, a, b, k):
    # initialize the array
    arr = [0] * n
    
    # update the array based on the queries
    for i in range(len(a)):
        arr[a[i]-1] += k[i]
        if b[i] < n:
            arr[b[i]] -= k[i]
    
    # calculate the maximum value in the array
    max_val = 0
    running_total = 0
    for val in arr:
        running_total += val
        if running_total > max_val:
            max_val = running_total
    
    return max_val

class boundaryValueAnalaysis(unittest.TestCase):

    def test_n_lower_bound(self):
        n = 2
        a = [1, 0, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_n_upper_bound(self):
        n = math.pow(10,9)
        a = [1, 0, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    
    def test_a_lower_than_1(self):
        n = 4
        a = [1, 0, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_a_greater_than_b(self):
        n = 4
        a = [1, 2, 3]
        b = [1, 1, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_b_lower_than_a(self):
        n = 4
        a = [1, 2, 3]
        b = [1, 1, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_b_lower_than_n(self):
        n = 4
        a = [1, 2, 3]
        b = [1, 5, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_k_lower_bound(self):
        n = 4
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [0, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_k_upper_bound(self):
        n = 4
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [10, 10, math.pow(10,9)]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_solution(self):
        n = 4
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), 30)

    
    
    # ======= n=math.pow(10,7) ========
    
    
    def test_a_lower_than_1_n_max(self):
        n = math.pow(10,7)
        a = [1, 0, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_a_greater_than_n_max_b(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [1, 1, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_b_lower_than_a_n_max(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [1, 1, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_b_lower_than_n_n_max(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [1, 5, 4]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_k_lower_bound_n_max(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [0, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_k_upper_bound_n_max(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [10, 10, math.pow(10,9)]
        self.assertEqual(arrayManipulation(n, a, b, k), -1)

    def test_solution_n_max(self):
        n = math.pow(10,7)
        a = [1, 2, 3]
        b = [3, 4, 5]
        k = [10, 10, 10]
        self.assertEqual(arrayManipulation(n, a, b, k), 30)


    # def test_a_greater_than_b(self):
    #     n = 5
    #     a = [3, 1, 4, 2, 5]
    #     b = [2, 3, 5, 4, 5]
    #     k = [10, 20, 30, 40, 50]
    #     with self.assertRaises(ValueError):
    #         arrayManipulation(n, a, b, k)

if __name__ == '__main__':
    unittest.main()
