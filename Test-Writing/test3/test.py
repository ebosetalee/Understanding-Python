import unittest
# from my_sum import sum
# OR for module :
target = __import__("my_sum")
sum = target.sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_sum_list_more_than_two_values_be_supplied(self):
        """
        Test that more than one value is provided
        """
        with self.assertRaises(TypeError):
            sum(1)
    
    def test_sum_value_is_not_negative(self):
        """
        Test that no value is in the negative
        """
        with self.assertRaises(TypeError):
            sum(1, 2, -3)

if __name__ == '__main__':
    unittest.main()