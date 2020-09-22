""" 
To convert the earlier example in `test1.py` to a unittest test case, you would have to:

1. Import unittest from the standard library
2. Create a class called TestSum that inherits from the TestCase class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the self.assertEqual() method on the TestCase class
5. Change the command-line entry point to call unittest.main()
"""

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 5, "Should be 5")

if __name__ == "__main__":
    unittest.main()

# This will print:
# ======================================================================
# FAIL: test_sum_tuple (__main__.TestSum)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/ella/Understanding-Python/Test-Writing/test2.py", line 20, in test_sum_tuple
#     self.assertEqual(sum((1, 2, 3)), 5, "Should be 5")
# AssertionError: 6 != 5 : Should be 5

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1) 

"""
While the following will print the output below:
"""
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == "__main__":
    unittest.main()

# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK