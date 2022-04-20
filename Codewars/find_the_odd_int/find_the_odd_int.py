# File: find_the_odd_int.py
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    # We will use list methods, so store seq as a list.
    seq_list = list(seq)

    for n in seq_list:
        if seq_list.count(n) % 2 == 1:
            return n
        else:
            pass
