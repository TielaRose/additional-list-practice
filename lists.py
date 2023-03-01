"""Additional List Practice

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""

def multiplication_table(n):
    """
    Returns a 2-D array containing an nxn multiplication table
    where n is the argument passed in
    """

    # TODO: replace this with your code

def find_common_items_minimum_index_sum(list1, list2):
    """
    Returns the common item(s) between the two lists which have the lowest index sum
    (the sum of the index of the item in each list.) If there is a tie, return all
    items with the lowest index sum.
    """

    # TODO: replace this with your code

def replace_elements(arr):
    """
    Replaces each element in arr with the greatest item among the elements to its right,
    and replace the last element with -1 since there are no elements to its right.
    For example [9,1,3,8] would turn into [9, 8, 8, -1].
    The input array arr will be modified and the function will return None.
    """

    # TODO: replace this with your code

def add_to_array_form(array_form_of_number, integer_to_add):
    """
    For a non-negative integer N, the array-form of N is an array of its digits in left to right order.
    Takes the array-form of a non-negative integer (`array_form_of_number`) as well as an integer to add to it (`integer_to_add`) and returns the array-form of their sum.
    """

    # TODO: replace this with your code

if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])