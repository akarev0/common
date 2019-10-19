import pytest
from unittest.mock import patch

from tests_practice.homework import (
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


def test_task_11_return_number_of_hours_and_minutes():
    num = task_11_number_of_hours_and_minutes(63)
    expected_num = "%d:%d" % (1, 3)
    assert num == expected_num


def test_task_12_return_first_largest_word_in_string():
    input_0 = task_12_first_largest_word_in_string("fun&!! time")
    input_1 = task_12_first_largest_word_in_string("I love dogs")
    result = "time"
    result_1 = "love"
    assert input_0 == result
    assert input_1 == result_1


@patch("builtins.input", return_value="Michele is name My")
def test_task_13_ask_and_print_back_with_the_backwards_order(mock):
    actual_result = task_13_ask_and_print_back_with_the_backwards_order()
    expected_result = "My name is Michele"
    assert actual_result == expected_result


@patch("builtins.input", return_value=3)
def test_task_14_how_many_Fibonnaci_numbers_to_generate(mock):
    result = task_14_how_many_fibonnaci_numbers()
    expected_result = [1, 1, 2]
    assert result == expected_result


def test_task_15_list_that_has_only_the_even_elements():
    given_list = task_15_list_that_has_only_the_even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    result_list = [4, 16, 36, 64, 100]
    assert given_list == result_list


@patch("builtins.input", return_value=4)
def test_task_16_numbers_from_1_to_input_number(mock):
    result = task_16_input_number()
    expected_result = 10
    assert result == expected_result


@patch("builtins.input", return_value=4)
def test_task_17(mock):
    actual_result = task_17_return_factorial()
    expected_result = 24
    assert actual_result == expected_result


def test_task_18_replace_every_letter_in_the_string():
    given_data = "abcd"
    actual_result = task_18_replace_every_letter_in_the_string(given_data)
    expected_result = "bcdE"
    assert actual_result == expected_result


def test_task_19_string_with_the_letters_in_alphabetical_order():
    input_string = task_19_string_with_the_letters_in_alphabetical_order("edcba")
    output_string = "abcde"
    assert input_string == output_string


def test_task_20_return_true_of_false():
    num1 = task_20_return_true_of_false(22, 25)
    num2 = task_20_return_true_of_false(23, 22)
    num3 = task_20_return_true_of_false(22, 22)
    assert num1 is True
    assert num2 is False
    assert num3 == "-1"
