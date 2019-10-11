import unittest
from unittest.mock import patch


from .homework import (
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
    task_11_number_of_hours_and_minutes,
    task_12_first_largest_word_in_string,
    task_13_ask_and_print_back_with_the_backwards_order,
    task_14_how_many_fibonnaci_numbers,
    task_15_list_that_has_only_the_even_elements,
    task_16_input_number,
    task_17_return_factorial,
    task_18_replace_every_letter_in_the_string,
    task_19_string_with_the_letters_in_alphabetical_order,
    task_20_return_true_of_false
)


class Test(unittest.TestCase):

    def test_list_without_duplicates(self):
        first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        results = [1, 2, 3, 5, 8, 13]
        self.assertEqual(list_without_duplicates(first_list, second_list), results)

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
        result_list = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(task_5_push_all_zeros(input_list), result_list)

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
        input_string = "Hello World and Coders"
        reversed_string = "sredoC dna dlroW olleH"
        self.assertEqual(task_10_return_the_string_in_reversed_order(input_string), reversed_string)

    def test_task_11_return_number_of_hours_and_minutes(self):
        num = 63
        self.assertEqual(task_11_number_of_hours_and_minutes(num), "%d:%d" % (1, 3))

    def test_task_12_return_first_largest_word_in_string(self):
        input_0 = "fun&!! time"
        input_1 = "I love dogs"
        self.assertEqual(task_12_first_largest_word_in_string(input_0), "time")
        self.assertEqual(task_12_first_largest_word_in_string(input_1), "love")

    @patch("builtins.input", return_value="Michele is name My")
    def test_task_13_ask_and_print_back_with_the_backwards_order(self, mock):
        actual_result = task_13_ask_and_print_back_with_the_backwards_order()
        expected_result = "My name is Michele"
        self.assertEqual(actual_result, expected_result)

    @patch("builtins.input", return_value=3)
    def test_task_14_how_many_Fibonnaci_numbers_to_generate(self, mock):
        result = task_14_how_many_fibonnaci_numbers()
        expected_result = [1, 1, 2]
        self.assertEqual(result, expected_result)

    def test_task_15_list_that_has_only_the_even_elements(self):
        given_list = task_15_list_that_has_only_the_even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        result_list = [4, 16, 36, 64, 100]
        self.assertEqual(given_list, result_list)

    @patch("builtins.input", return_value=4)
    def test_task_16_numbers_from_1_to_input_number(self, mock):
        result = task_16_input_number()
        expected_result = 10
        self.assertEqual(result, expected_result)

    @patch("builtins.input", return_value=4)
    def test_task_17(self, mock):
        actual_result = task_17_return_factorial()
        expected_result = 24
        self.assertEqual(actual_result, expected_result)

    def test_task_18_replace_every_letter_in_the_string(self):
        given_data = "abcd"
        actual_result = task_18_replace_every_letter_in_the_string(given_data)
        expected_result = "bcdE"
        self.assertEqual(actual_result, expected_result)

    def test_task_19_string_with_the_letters_in_alphabetical_order(self):
        input_string = task_19_string_with_the_letters_in_alphabetical_order("edcba")
        output_string = "abcde"
        self.assertEqual(input_string, output_string)

    def test_task_20_return_true_of_false(self):
        num1 = task_20_return_true_of_false(22, 25)
        num2 = task_20_return_true_of_false(23, 22)
        num3 = task_20_return_true_of_false(22, 22)
        self.assertTrue(num1)
        self.assertFalse(num2)
        self.assertEqual(num3, "-1")


if __name__ == "__main__":
    unittest.main()

