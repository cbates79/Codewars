# File: scramblies.py
'''
Complete the function scramble(str1, str2) that returns true if a portion of 
str1 characters can be rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will 
be included. Performance needs to be considered.

Examples:
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''
def scramble(s1, s2):
    if not(s2.isalpha() and s2.lower()):
        raise ValueError(f"Argument {s2} is not only lowercase letters.")
    else:
        skip_letters = list()
        target_dict = dict()
        for x in s2:
            if x not in skip_letters:
                skip_letters.append(x)
                target_dict[x] = s2.count(x)
                if s1.count(x) < target_dict[x]:
                    return False
        return True
'''
    if not(s2.isalpha() and s2.lower()):
        raise ValueError(f"Argument {s2} is not only lowercase letters.")
    else:
        for x in s2:
            if s1.count(x) < s2.count(x):
                return False
        return True
'''
'''
    target = list(s2)
    source = list(s1)
    for x in target:
        if x in source:
            count_in_target = target.count(x)
            count_in_source = source.count(x)
            if count_in_target <= count_in_source:
                for i in range(count_in_target):
                    target.remove(x)
                    source.remove(x)
            else:
                return False
        else:
            return False
    return True
'''
