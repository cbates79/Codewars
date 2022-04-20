# File: equal_sides_of_an_array.py
# You are going to be given an array of integers. Your job is to take that 
# array and find an index N where the sum of the integers to the left of N 
# is equal to the sum of the integers to the right of N. If there is no index 
# that would make this happen, return -1.

def find_even_index(arr):
    indices = range(len(arr))

    # Edge cases:
    # len(arr) == 0:
    # len(arr) == 1:
    # len(arr) == 2:

    for index in indices:
        left_sum = sum(arr[:index])
        right_sum = sum(arr[index - 1:])
