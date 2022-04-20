# File: maximum_subarray_sum.py
'''
The maximum sum subarray problem consists in finding the maximum sum of 
a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the 
maximum sum is the sum of the whole array. If the list is made up of 
only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list 
or array is also a valid sublist/subarray.

'''
def max_sequence(arr):
    arr_list = list(arr)
    for x in arr_list:
        if type(x) != int:
            raise ValueError(f"Element {x} is not of type int.")
    if len(arr_list) == 0:
        return 0
    else:
        all_negative = True
        for x in arr_list:
            if x >= 0:
                all_negative = False
        if all_negative:
            return 0
        else:
            max_sum = 0
            for i in range(len(arr_list) + 1):
                for j in range(len(arr_list) + 1):
                    if i <= j:
                        temp_sum = sum(arr_list[i:j])
                        if temp_sum > max_sum:
                            max_sum = temp_sum
            return max_sum

