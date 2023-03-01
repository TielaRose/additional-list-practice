"""Additional List Practice

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""

def multiplication_table(n):
    """
    Return a 2-D array containing an nxn multiplication table
    where n is the argument passed in
    """

    return [[i * j for i in range(1, n+1)] for j in range(1,n+1)]

def find_common_items_minimum_index_sum(list1, list2):
    """
    Return the common item(s) between the two lists which have the lowest index sum
    (the sum of the index of the item in each list.) If there is a tie, return all
    items with the lowest index sum.
    """
    list1_to_index = { restaurant: index for index, restaurant in enumerate(list1)} # dictionary comprehension
    result = []
    min_index_sum = len(list1) + len(list2) # the min index will always be smaller than this
    for index, restaurant in enumerate(list2):
        if restaurant in list1_to_index:
            cur_index_sum = list1_to_index[restaurant] + index
            if cur_index_sum < min_index_sum:
                min_index_sum = cur_index_sum
                result = [restaurant]
            elif cur_index_sum == min_index_sum:
                result.append(restaurant)
    return result

def replace_elements(arr):
    """
    Replaces each element in arr with the greatest item among the elements to its right,
    and replace the last element with -1 since there are no elements to its right.
    For example [9,1,3,8] would turn into [9, 8, 8, -1].
    The input array arr will be modified and the function will return None.
    """
    curMax = arr[-1]
    arr[-1] = -1 # the last element will be replaced by -1
    current_index = -2
    for num in arr[-2::-1]: # from the 2nd to last element to the beginning, in reverse order
        arr[current_index] = curMax
        if num > curMax:
            curMax = num
        current_index -= 1

def add_to_array_form(array_form_of_number, integer_to_add):
    """
    For a non-negative integer N, the array-form of N is an array of its digits in left to right order.
    Takes the array-form of a non-negative integer (`array_form_of_number`) as well as an integer to add to it (`integer_to_add`) and returns the array-form of their sum.
    """

    result = []
    carry = 0
    second_number_array_form = [int(digit) for digit in list(str(integer_to_add))]
    max_number_length = max(len(array_form_of_number), len(second_number_array_form))
    # pad the shorter number with leading 0s so the arrays are the same length
    array_form_of_number = [0]*(max_number_length - len(array_form_of_number)) + array_form_of_number[:max_number_length]
    second_number_array_form = [0]*(max_number_length - len(second_number_array_form)) + second_number_array_form[:max_number_length]
    for index, num in enumerate(array_form_of_number[::-1]):
        actual_index = len(array_form_of_number) - index - 1
        current = num + second_number_array_form[actual_index] + carry
        result = [(current % 10)] + result
        carry = current // 10
    if carry:
        result = [carry] + result
    return result

if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])