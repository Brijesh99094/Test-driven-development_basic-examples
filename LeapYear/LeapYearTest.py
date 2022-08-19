
import unittest
from LeapYearMain import CheackYear

class LeapYearTest(unittest.TestCase):

    def setUp(self) :
        self.chk_year = CheackYear()
    
    def test_isDivisibleByFourHundread(self):
        self.assertTrue(self.chk_year.isLeapYear(2000),"Must be divisible by 400" )

    def test_isDivisibleByHundreadAndNotByFourHundread(self):
        self.assertFalse(self.chk_year.isLeapYear(1700),"Must be divisible by 100 but not by 400") 

    def test_isDivisibleByFourAndNotByHundread(self):
        self.assertTrue(self.chk_year.isLeapYear(2008),"Must be divisible by 4 but not by 100")

    def test_isDivisibleByFour(self):
        self.assertTrue(self.chk_year.isLeapYear(2012),"Must be divisible by 4 only")

if __name__ == "__main__":
    unittest.main()
