# TESTING

There are many ways to test your code.
The shortest, simplest way of running the test suite is the following command from the root directory of your checkout (terminal).

`./python -m test`

- __Exploratory testing__ is a form of testing that is done without a plan. In an exploratory test, you’re just exploring the application.
To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it.

- This is where automated testing comes in.
__Automated testing__ is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human.

### Automated testing.

Generally, when the development process is complete, the developer codes criteria, or the results that are known to be potentially practical and useful, into the test script to verify a particular unit's correctness. During test case execution, various frameworks log tests that fail any criterion and report them in a summary.
The developers are expected to write automated test scripts, which ensures that each and every section or a unit meets its design and behaves as expected.

__Two types of Automated tests:__
1. An integration test checks that components in your application operate with each other.
2. A unit test checks a small component in your application.
You can write both integration tests and unit tests in Python.

__Integration testing__
Testing multiple components is known as integration testing.

There are many test runners which depends on your requirements and level of experience is important. They include:
1. unittest
2. nose or nose2
3. pytest

__PYTEST__
`pytest` supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.

PYTEST has some other great features:
- Support for the built-in assert statement instead of using special s`elf.assert*()` methods
- Support for filtering for test cases
- Ability to rerun from the last failing test
- An ecosystem of hundreds of plugins to extend the functionality

__Writing the TestSum test case example for pytest would look like this:__
```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5" 
```

## UNITTEST

The unit test framework in Python is called `unittest`, which comes packaged with Python. In other words, it has been built into the Python standard library since version 2.1.
A unit test is a smaller test, one that checks that a single component operates in the right way. It helps to isolate what is broken in your application and fix it faster.
Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use. It determines and ascertains the quality of your code.

__unittest requires that:__

- You put your tests into classes as methods
- You use a series of special assertion methods in the `unittest.TestCase` class instead of the built-in assert statement

__Implementing `unittest` as seen in test2.py:__
1. Import unittest from the standard library
2. Create a class called TestSum that inherits from the TestCase class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the self.assertEqual() method on the TestCase class
5. Change the command-line entry point to call unittest.main()

__HOW TO WRITE ASSERTIONS:__
Method |  Equivalent to
- .assertEqual(a, b) |	a == b
- .assertTrue(x)	| bool(x) is True
- .assertFalse(x)	| bool(x) is False
- .assertIs(a, b)	| a is b
- .assertIsNot(a, b) |  a is not b
- .assertIsNone(x) |	x is None
- .assertIsNotNone(x) | x is not None
- .assertIn(a, b) |	a in b
- .assertIsInstance(a, b) |	isinstance(a, b)
- .assertRaises(TypeError) | Raises(TypeError)
- .assertAlmostEqual(x(a), b) | x(a) is abbr. == b
- .assertNotEqual(a, b) | a != b
- .assertGreater(a, b) | a > b
- .assertGreaterEqual(a, b) | a >= b
- .assertRegex(s, r) | r.search(s)
- .assertNotRegex(s, r) | not r.search(s)
- .assertCountEqual(a, b)
- etc.

.assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), .assertNotIsInstance(), .asserLess(), .assertLessEqual and so forth...
