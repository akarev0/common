import unittest
import pytest
from unittest.mock import patch

from tests_practice.homework import (
    list_without_duplicates,
    number_of_times,
    integer_is_a_power_of_three,
    add_the_digits_of_a_positive_integer,
    task_5_push_all_zeros,
    task_6_check_a_sequence_of_number,
    task_7_number_that_doesnt_occur_twice,
    task_8_find_a_missing_number_from_a_list,
    task_9_count_the_elements_in_a_list_until_an_element_is_a_tuple,
    task_10_return_the_string_in_reversed_order,

)


class Test(unittest.TestCase):

    def test_list_without_duplicates(self):
        first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        results = [1, 2, 3, 5, 8, 13]
        third_list = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(list_without_duplicates(first_list, second_list), results)
        self.assertEqual(list_without_duplicates(first_list, third_list), results)

    def test_number_of_times(self):
        sentence = "I am a good developer. I am also a writer"
        self.assertEqual(number_of_times(sentence), 5)

    def test_integer_is_a_power_of_three(self):
        integer_1 = 12
        integer_2 = 27
        self.assertTrue(integer_is_a_power_of_three(integer_2))
        self.assertFalse(integer_is_a_power_of_three(integer_1))

    def test_add_the_digits_of_a_positive_integer(self):
        digit_1 = 123
        digit_2 = 34
        self.assertEqual(add_the_digits_of_a_positive_integer(digit_1), 6)
        self.assertEqual(add_the_digits_of_a_positive_integer(digit_2), 7)

    def test_task_5_push_all_zeros(self):
        input_list = [0, 2, 3, 4, 6, 7, 10]
        input_list_1 = [0, 2, 0, 3, 4, 6, 7, 10]
        result_list = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(task_5_push_all_zeros(input_list), result_list)
        self.assertEqual(task_5_push_all_zeros(input_list_1), result_list)

    def test_task_6_check_a_sequence_of_number(self):
        input_data = [5, 7, 9, 11]
        input_data_1 = [3, 5, 9, 14]
        self.assertTrue(task_6_check_a_sequence_of_number(input_data))
        self.assertFalse(task_6_check_a_sequence_of_number(input_data_1))

    def test_task_7_number_that_doesnt_occur_twice(self):
        input_data = [5, 3, 4, 3, 4]
        input_data_1 = [3, 4, 3, 4]
        self.assertEqual(task_7_number_that_doesnt_occur_twice(input_data), 5)
        self.assertNotEqual(task_7_number_that_doesnt_occur_twice(input_data_1), 0)

    def test_task_8_find_a_missing_number_from_a_list(self):
        input_data = [1, 2, 3, 4, 6, 7, 8]
        self.assertEqual(task_8_find_a_missing_number_from_a_list(input_data), 5)

    def test_task_9_count_the_elements_in_a_list_until_an_element_is_a_tuple(self):
        input_data = [1, 2, 3, (1, 2), 3]
        self.assertEqual(task_9_count_the_elements_in_a_list_until_an_element_is_a_tuple(input_data), 3)

    def test_task_10_return_the_string_in_reversed_order(self):
        input_string = task_10_return_the_string_in_reversed_order("Hello World and Coders")
        reversed_string = "sredoC dna dlroW olleH"
        assert input_string == reversed_string



if __name__ == "__main__":
    unittest.main()

