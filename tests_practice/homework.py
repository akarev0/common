
import math

from string import punctuation


def list_without_duplicates(list1, list2):
    result_list = []
    result = []
    for i in list1:
        for k in list2:
            if i == k:
                result_list.append(i)
    for num in result_list:
        if num not in result:
            result.append(num)
    return result


def number_of_times(sentence):
    return sentence.count('a')



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


def task_11_number_of_hours_and_minutes(num):
    hour = num // 60
    minutes = num % 60
    return "%d:%d" % (hour, minutes)


def task_12_first_largest_word_in_string(input_str):
    input_str = "".join(ch for ch in input_str if ch not in punctuation)
    return max(input_str.split(), key=len)


def task_13_ask_and_print_back_with_the_backwards_order():
    input_str = input("Enter the string: ")
    input_str = ' '.join(reversed(input_str.split()))
    return input_str


def task_14_how_many_fibonnaci_numbers():
    num = int(input("How many Fibonnaci numbers do you want to generate? "))
    result = [1]
    for i in range(num - 1):
        if i == 0:
            result.append(1)
        else:
            result.append(result[i] + result[i - 1])
    return result


def task_15_list_that_has_only_the_even_elements(given_data):
    return [x for x in given_data if x % 2 == 0]


def task_16_input_number():
    num = int(input("Enter integer: "))
    return sum(range(num + 1))


def task_17_return_factorial():
    num = int(input("Factorial?: "))
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact


def task_18_replace_every_letter_in_the_string(given_data):

    a = 'aeiou'
    new_string = []
    for word in given_data:
        for char in word:
            if char != ' ':
                char = 'a' if char == 'z' else chr(ord(char) + 1)
                char = char.upper() if char in a else char
            else:
                char = ' '
            new_string.append(char)
    return ''.join(new_string)


def task_19_string_with_the_letters_in_alphabetical_order(input_string):
    str_split = []
    for i in range(len(input_string)):
        str_split.append(input_string[i])
    str_split.sort()
    new_str = "".join(str_split)
    return new_str


def task_20_return_true_of_false(num1, num2):

    if num1 == num2:
        return str(-1)
    elif num1 < num2:
        return True
    else:
        return False




