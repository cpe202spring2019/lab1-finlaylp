import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        nums = [1,2,4,9,1]
        nums2 = [3,3,3,3]
        self.assertEqual(max_list_iter(nums),9)
        self.assertEqual(max_list_iter(nums2),3) #tests for the max in a list of all the same values   
        self.assertEqual(max_list_iter([-2,-4,-6,-1]), -1) #tests for max in a list of only negative values
        self.assertEqual(max_list_iter([]),None)#tests for the case when the list is empty
        with self.assertRaises(ValueError):
           max_list_iter(None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        tlist = None #this tests for when there is a value error
        with self.assertRaises(ValueError):
           reverse_rec(tlist)
        self.assertEqual(reverse_rec([0,3,4,6]),[6,4,3,0]) #an additional test for reversing the list

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
  
        with self.assertRaises(ValueError):
           bin_search(5,0, 10, None)
        
        list2 = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bin_search(2,0, 9, list2), 1)


if __name__ == "__main__":
        unittest.main()

    
