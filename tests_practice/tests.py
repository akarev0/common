import unittest

from tests_practice.homework import list_without_duplicates


class Test(unittest.TestCase):

    def test_list_without_duplicates(self):
        first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        results = [1, 2, 3, 5, 8, 13]
        self.assertEqual(list_without_duplicates(first_list, second_list), results)


if __name__ == "__main__":
    unittest.main()

