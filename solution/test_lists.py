"""Tests for lists.py"""

from lists import (
    multiplication_table,
    find_common_items_minimum_index_sum,
    replace_elements,
    add_to_array_form,
)

def test_multiplication_table_three():
    """Test that the return value of get_words_by_first_letter is a list."""
    assert multiplication_table(3) == [[1,2,3],[2,4,6],[3,6,9]]

def test_multiplication_table_empty():
    """Test that get_words_by_first_letter returns words that start with a certain letter."""
    assert multiplication_table(0) == []

def test_find_common_items_minimum_index_sum_1():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    assert find_common_items_minimum_index_sum(list1, list2) == ["Shogun"]

def test_find_common_items_minimum_index_sum_2():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    assert find_common_items_minimum_index_sum(list1, list2) == ["Shogun"]

def test_find_common_items_minimum_index_sum_3():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
     # use set to make sure order does not affect test outcome
    assert set(find_common_items_minimum_index_sum(list1, list2)) == set(["KFC","Burger King","Tapioca Express","Shogun"])

def test_find_common_items_minimum_index_sum_4():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
     # use set to make sure order does not affect test outcome
    assert set(find_common_items_minimum_index_sum(list1, list2)) == set(["KFC","Burger King","Tapioca Express","Shogun"])

def test_find_common_items_minimum_index_sum_5():
    list1 = ["KFC"]
    list2 = ["KFC"]
    assert find_common_items_minimum_index_sum(list1, list2) == ["KFC"]

def test_replace_elements_multiple():
    arr = [17,18,5,4,6,1]
    assert replace_elements(arr) == None
    assert arr == [18,6,6,6,1,-1]

def test_replace_elements_single():
    arr = [400]
    assert replace_elements(arr) == None
    assert arr == [-1]

def test_add_to_array_form_1():
    assert add_to_array_form( [1,2,0,0], 34) == [1,2,3,4]

def test_add_to_array_form_2():
    assert add_to_array_form([2,7,4], 181) == [4,5,5]

def test_add_to_array_form_3():
    assert add_to_array_form([2,1,5], 806) == [1,0,2,1]

def test_add_to_array_form_4():
    assert add_to_array_form( [9,9,9,9,9,9,9,9,9,9], 1) == [1,0,0,0,0,0,0,0,0,0,0]