import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(-1, 1), 0)
        self.assertEqual(SimpleMath.addition(0, 0), 0)

    def test_soustraction(self):
        self.assertEqual(SimpleMath.soustraction(5, 2), 3)
        self.assertEqual(SimpleMath.soustraction(10, 10), 0)
        self.assertEqual(SimpleMath.soustraction(0, 5), -5)

if __name__ == '__main__':
    unittest.main()