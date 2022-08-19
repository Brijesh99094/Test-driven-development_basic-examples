import unittest

from EmployeeClass import Employee 


class TestEmployee(unittest.TestCase):

    

    def setUp(self) :
        print("setUp")
        self.emp_1 = Employee("brijesh","prajapati",53000)
        self.emp_2 = Employee("dharmil","shah",50000)

    def tearDown(self) :
        print("tearDown")
    
    def test_emailShouldChangeAccordingToFirstAndLastName(self):
        self.assertEqual(self.emp_1.email,"brijeshprajapati@gmail.com","Must  return email consisting first name and last  name")
        self.assertEqual(self.emp_2.email,"dharmilshah@gmail.com","Must  return email consisting first name and last  name")

    def test_fullnameShouldReturnFirstNameAndLastNameTogether(self):
        self.assertEqual(self.emp_1.fullname,"brijesh prajapati","Must return fullname")
        self.assertEqual(self.emp_2.fullname,"dharmil shah","Must return fullname")

    def test_payShouldbeRaisedByFivePercent(self):
        self.assertEqual(self.emp_1.raise_pay(),55650,"Must raised by five percent")
        self.assertEqual(self.emp_2.raise_pay(),52500,"Must raised by five percent")

if __name__  == "__main__":
    unittest.main()


