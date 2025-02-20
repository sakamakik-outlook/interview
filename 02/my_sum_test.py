import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        # write unit test and check sum([1,2,3]) returns 6


if __name__ == '__main__':
    unittest.main()