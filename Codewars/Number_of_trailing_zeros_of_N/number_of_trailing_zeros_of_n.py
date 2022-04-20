# File: number_of_trailing_zeros_of_n.py
'''
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

Examples:

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial. Find another way to 
find the number of zeros.
'''
from math import *
def zeros(n):
    if type(n) != int:
        raise ValueError(f"Argument {n} is not an int")
    elif n < 0:
        raise ValueError(f"Argument {n}<0")
    elif n == 0:
        return 0
    else:
        number_of_zeros = 0
        for k in range(1, 1 + floor(log(n, 5))):
            number_of_zeros += floor(n / pow(5, k))
        return number_of_zeros
        '''
        factors_of_2 = 0
        factors_of_5 = 0
        for f in range(1, n + 1):
            while f >= 5 and f % 5 == 0:
                factors_of_5 += 1
                f /= 5
            while f >= 2 and f % 2 == 0:
                factors_of_2 += 1
                f /= 2
        return min(factors_of_2, factors_of_5)
        '''
