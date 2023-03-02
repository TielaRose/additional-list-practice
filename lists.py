"""Additional List Practice

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""


def multiplication_table(n):
    """
    Returns a 2-D array containing an nxn multiplication table
    where n is the argument passed in
    """

    # ex: n = 3
    # result = [[1, 2, 3],
    #           [2, 4, 6],
    #           [3, 6, 9]]

    # initialize an empty result list
    result = []

    # initialize an empty top row list, listing each number from 1 - n
    if n != 0:
        row1 = [num for num in range(1, n + 1)]

        # append that row to the result list
        result.append(row1)

        for i in range(2, n+1):  # loop over the numbers 2, 3...n
            row = [num * i for num in row1]  # create the next row
            result.append(row)  # append that row to the result list

    return result

    # hackbright solution
    # return [[i * j for i in range(1, n+1)] for j in range(1, n+1)]

    # example: n = 3
    # the inner part loops over i each time (i = 1, 2, 3) for EACH j (starting at j=1)

    # so first j = 1, and we loop through all the i values
    # [1 * 1, 2 * 1, 3 * 1] -> [1, 2, 3]

    # then j = 2, and we loop again through the i values
    # [1 * 2, 2 * 2, 3 * 2] -> [2, 4, 6]

    # last j = 3, and we loop through the i values
    # [1 * 3, 2 * 3, 3 * 3] -> [3, 6, 9]


def find_common_items_minimum_index_sum(list1, list2):
    """
    Returns the common item(s) between the two lists which have the lowest index sum
    (the sum of the index of the item in each list.) If there is a tie, return all
    items with the lowest index sum.
    """

    common_items = []  # Initialize a list to hold the commmon item(s)

    list1_len = len(list1)
    list2_len = len(list2)
    # Set index_sum to the max it could be for these two lists
    min_index_sum = list1_len + list2_len - 2

    # Find out which list is shorter
    if list1_len < list2_len:
        smaller = list1
        bigger = list2
    else:
        smaller = list2
        bigger = list1

    # Iterate over the smaller list
    for item in smaller:
        if item in bigger:
            # Find the index of the item in the smaller list
            ind_smaller = smaller.index(item)
            # Find the index of the item in the bigger list
            ind_bigger = bigger.index(item)
            # Initialize a new variable for the sum of these indices
            curr_index_sum = ind_smaller + ind_bigger
            # Compare the sum of these indices to the current "lowest sum" (index_sum)
            if curr_index_sum < min_index_sum:
                # If it's lower, replace the common items
                min_index_sum = curr_index_sum
                common_items[:] = [item]
            elif curr_index_sum == min_index_sum:  # If it's the same, add it to the common items list
                common_items.append(item)

    # Return the list of common items
    return common_items


def replace_elements(arr):
    """
    Replaces each element in arr with the greatest item among the elements to its right,
    and replace the last element with -1 since there are no elements to its right.
    For example [9,1,3,8] would turn into [8, 8, 8, -1].
    The input array arr will be modified and the function will return None.
    """

    # # my first solution

    # # loop over the array
    # for index, _ in enumerate(arr):
    #     if arr[index] == arr[-1]:  # set the last item to -1
    #         arr[index] = -1
    #         break
    #     else:  # look for the max to the right of each item, set that item to that max
    #         arr[index] = max(arr[index + 1:])

    # this solution technically works, but is ineffcient in a few ways:
    # 1) it checks EVERY item to see if it's the last item. Seems like I should do this only once
    # 2) it rechecks the max of everything else EVERY time. Seems like I should be able to keep track of the max

    # what if I went backwards? [17, 18, 5, 4, 6, 1] --> [18, 6, 6, 6, 1, -1]
    curr_max = arr[-1]  # set the max to the last item in the array
    arr[-1] = -1  # set that last item to -1

    # loop through the array backwards, starting from the second-to-last item
    curr_index = -2
    for num in arr[-2::-1]:
        arr[curr_index] = curr_max  # set the current item to the current max
        if num > curr_max:
            curr_max = num
        curr_index -= 1


def add_to_array_form(array_form_of_number, integer_to_add):
    """
    For a non-negative integer N, the array-form of N is an array of its digits in left to right order.
    Takes the array-form of a non-negative integer (`array_form_of_number`) as well as an integer to add to it (`integer_to_add`) and returns the array-form of their sum.
    """

    # ex: array_form_of_number = [4, 9, 7, 2]
    # ex: integer_to_add = 64
    # Unclear from this function stub if I'm supposed to modify the input array or not. To be safe, I won't modify it.
    # Make a copy of the input array
    sum_array = array_form_of_number[:]

    # Loop over the input array, starting from the end
    index = -1
    while integer_to_add > 0:
        digit_to_add = integer_to_add % 10  # Get the final digit of the integer_to_add
        integer_to_add = integer_to_add // 10  # Remove that integer from integer_to_add

        # If the index has surpassed the length of the original input array, then the first (leftmost) digit of the sum array should be 1, and we can end the loop
        if index * -1 > len(array_form_of_number):
            sum_array[0:0] = [1]
            break
        else:
            total = sum_array[index] + digit_to_add  # Add the digits

            if total < 10:  # If the sum is less than 10, replace the number with the sum
                sum_array[index] = total
            else:  # If the sum is greater than 10, replace the number with the ones digit, and 'carry' the 1
                sum_array[index] = total - 10
                integer_to_add += 1

            index -= 1  # Decrement the index to go to the next digit to the left

    return sum_array


if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])
