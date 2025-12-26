import unittest
from py_scripts.math_ops import square_number

class TestMathOps(unittest.TestCase):
    def test_square_number(self):
        print(f"Testing square_number(4) → Expected: 16, Actual: {square_number(4)}")
        print(f"Testing square_number(0) → Expected: 0, Actual: {square_number(0)}")
        print(f"Testing square_number(-3) → Expected: 9, Actual: {square_number(-3)}")

        self.assertEqual(square_number(4), 16)
        self.assertEqual(square_number(0), 0)
        self.assertEqual(square_number(-3), 9)

if __name__ == '__main__':
    unittest.main()
