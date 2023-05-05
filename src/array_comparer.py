import unittest

class ArrayComparer:
    def compare_arrays(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        for elem in arr1:
            if elem not in arr2:
                return False
        return True

class TestArrayComparer(unittest.TestCase):
    def setUp(self):
        self.arr1 = [1,2,3]
        self.arr2 = [3,2,1]
        self.arr3 = [1,2,4]
    
    def equivalancePartitioning(self):
        array_comparer = ArrayComparer()
        self.assertTrue(array_comparer.compare_arrays(self.arr1, self.arr2))
        self.assertFalse(array_comparer.compare_arrays(self.arr1, self.arr3))

if __name__ == '__main__':
    unittest.main()