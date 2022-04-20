# File: digital_root.py
# Given n, take the sum of the digits of n. If that value has more than 
# one digit, continue reducing in this way until a single-digit number
# is produced. The input will be a non-negative integer.

def digital_root(n):
    # Store the digits of n and compute their sum them.
    n_string = str(n)
    digits_tuple = tuple()
    for digit in n_string:
        digits_tuple += (int(digit),)

    if len(digits_tuple) == 1:
        return digits_tuple[0]
    elif len(digits_tuple) > 1:
        return digital_root(sum(digits_tuple))
    else:
        print(f"Error: unable to compute digital root of {n}.")
