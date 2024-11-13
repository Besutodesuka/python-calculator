import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)

    # Test cases for subtract()
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
        self.assertEqual(self.calc.subtract(3, 7), -4)

    # Test cases for multiply()
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 12), 36)
        self.assertEqual(self.calc.multiply(-4, 7), -28)

    # Test cases for divide()
    def test_divide(self):
        self.assertEqual(self.calc.divide(16, 4), 4)
        self.assertEqual(self.calc.divide(-7, 1), -7)

    # Test cases for modulo()
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(57, 2), 1)
        self.assertEqual(self.calc.modulo(55, 5), 0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()