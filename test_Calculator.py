import unittest 
from calculator import Calculator 
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c=Calculator()
    def test_add(self):
        self.assertEqual(self.c.add(1,1),2)
    def test_subtraction(self):
        self.assertEqual(self.c.subtract(4,3),1)
    def test_multiply(self):
        self.assertEqual(self.c.multiply(2,2),4)
    def test_divide(self):
        self.assertRaises(ValueError)
        self.assertEqual(self.c.divide(10,5),2)
        self.assertEqual(self.c.divide(20,0))

if __name__=='__main__':
    unittest.main()
