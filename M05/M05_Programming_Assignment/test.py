import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
    
""" 
All the tests ran before the fraction code was added resulted in an OK because 1+2+3 equals 6. 
After the fraction code was added the test resulted in a fail. This is beacuse the sum of the three fractions doesn't equal 1. 
"""