# File: ip_validation.py
'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal 
format. IPs should be considered valid if they consist of four octets, with 
values between 0 and 255, inclusive.

Valid inputs examples:
1.2.3.4
123.45.67.89

Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
'''
def is_valid_IP(strng):
    valid_range = range(256)
    word_list = strng.split('.')
'''    is_octet = bool(len(word_list) == 4)
    if not is_octet:
        return False
    else:
        for word in word_list:
            if not word.isnumeric():
                return False
            elif int(word) not in valid_range:
                return False
            else:
                return True
'''
