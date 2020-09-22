assert sum([1, 2, 3]) == 6, "Should be 6"

# This will not output anything on the terminal because the values are correct.

# assert sum([1, 2, 1]) == 6, "Should be 6"
""" 
this will produce error as follows:
line 5, in <module>
assert sum([1, 2, 1]) == 6, "Should be 6"
AssertionError: Should be 6

It raised AssertionError because the result 
of sum() does not match 6.
"""

# To write a test case, an assertion, and an entry point:
# Write the following in a python file "test_sum.py":
"""__name__ = "test_sum" is used when the file to be tested 
    is imported into the test.
"""

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")