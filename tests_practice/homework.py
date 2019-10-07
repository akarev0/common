import math


def list_without_duplicates(list1, list2):
    result_list = []
    results = []
    for i in list1:
        for k in list2:
            if i == k:
                result_list.append(i)
    for j in result_list:
        if j not in results:
            results.append(j)
    return results


def number_of_times(sentence):
    num_count = sentence.count('a')
    return num_count


def integer_is_a_power_of_three(number):
    integer = (math.log(number, 3))
    return int(integer) == integer


def add_the_digits_of_a_positive_integer(digit):
    return (digit - 1) % 9 + 1 if digit > 0 else 0


def task_5_push_all_zeros(input_list):
    res_list = [i for i in input_list if i != 0]
    res_list.append(0)
    return res_list


def task_6_check_a_sequence_of_number(input_data):
    i = 0
    if input_data[i + 1] - input_data[i] == input_data[i + 2] - input_data[i + 1]:
        return True


def task_7_number_that_doesnt_occur_twice(input_data):
    result = 0
    for i in input_data:
        result ^= i
        return result


def task_8_find_a_missing_number_from_a_list(input_data):
    n = len(input_data)
    total = (n + 1) * (n + 2) / 2
    sum_number_form_a_list = sum(input_data)
    return total - sum_number_form_a_list


def task_9_count_the_elements_in_a_list_until_an_element_is_a_tuple(data):
    count = 0
    for i in data:
        if isinstance(i, tuple):
            break
        count += 1
    return count


def task_10_return_the_string_in_reversed_order(some_string):
    string = "".join(reversed(some_string))
    return string

