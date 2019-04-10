import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        
        loc1 = Location("Bay Area", -90, -90)
        self.assertEqual(repr(loc1), "Location('Bay Area', -90, -90)") 
    
    # Add more tests!
    def test_eq(self):    
        loc1 = Location("CA", 50, 50)
        loc2 = Location("CA", 50, 50)
        self.assertEqual(loc1,loc2)        

        loc3 = Location("SLO", -70, -90)
        loc4 = Location("SLO", -70, -90)
        self.assertEqual(loc3,loc4)
        
        self.assertNotEqual(loc1,loc3)        

if __name__ == "__main__":
        unittest.main()
