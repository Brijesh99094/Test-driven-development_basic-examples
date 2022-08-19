



import unittest 
from FizzBuzzMain import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    # this method is used when you want to create something before each test is executed by test runner
    def setUp(self): # this is like before in java
        self.fb = FizzBuzz()

    # this method is used when you want to do something after the each test execution. 
    def tearDown(self):
        pass

    

    def test_numberShouldDevisibleByThree(self):
        self.assertEqual(self.fb.fizz_buzz_or_number(9),"Fizz","Must be divisible  by 3")

    def test_numberShouldDivisibleByFive(self):
        self.assertEqual(self.fb.fizz_buzz_or_number(50),"Buzz",'Must be divisible by Five')

    def test_numberShouldDivisibleBYThreeAndFive(self):
        self.assertEqual(self.fb.fizz_buzz_or_number(15),"FizzBuzz",'Must be divisible by three and five')

    def test_numberNotDivisibleByThreeAndFive(self):
        inputNumber = 11
        self.assertEqual(self.fb.fizz_buzz_or_number(11),str(inputNumber),"Not divisible by three and five")
        pass
if __name__ == "__main__":
    unittest.main()