# File: vowel_count.py
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0
    for v in vowels:
        counter += sentence.count(v)

    return counter
