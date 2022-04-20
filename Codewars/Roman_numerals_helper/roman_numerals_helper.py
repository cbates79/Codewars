# File: roman_numerals_helper.py
'''
Create a RomanNumerals class that can convert a roman numeral to and from 
an integer value. It should follow the API demonstrated in the examples 
below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately 
starting with the left most digit and skipping any digit with a value of 
zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting 
in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each 
Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's 
four").

Examples:
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000

Help:
Symbol 	Value
I 	1
IV 	4
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000
'''
class RomanNumerals:
    symbols = ('I', 'IV', 'V', 'X', 'L', 'C', 'D', 'M')
    values = (1, 4, 5, 10, 50, 100, 500, 1000)

    symbol_to_value = dict(zip(symbols, values))
    value_to_symbol = dict(zip(values, symbols))

    def to_roman(val):
        roman_output = ''
        val_string = str(val)
        temp = 0
        
        # Process thousands place.
        if len(val_string) > 3:
            thousands_digit = int(val_string[-4])
            temp = thousands_digit
            for i in range(temp):
                roman_output += RomanNumerals.value_to_symbol[1000]

        # Process hundreds place.
        if len(val_string) > 2:
            hundreds_digit = int(val_string[-3])
            temp = hundreds_digit
        if temp == 9:
            roman_output += RomanNumerals.value_to_symbol[100]
            roman_output += RomanNumerals.value_to_symbol[1000]
            temp = 0
        if temp >= 5:
            roman_output += RomanNumerals.value_to_symbol[500]
            temp -= 5
        if temp == 4:
            roman_output += RomanNumerals.value_to_symbol[100]
            roman_output += RomanNumerals.value_to_symbol[500]
            temp -= 4
        if temp in range(1, 4):
            for i in range(temp):
                roman_output += RomanNumerals.value_to_symbol[100]
        
        # Process tens place.
        if len(val_string) > 1:
            tens_digit = int(val_string[-2])
            temp = tens_digit
        if temp == 9:
            roman_output += RomanNumerals.value_to_symbol[10]
            roman_output += RomanNumerals.value_to_symbol[100]
            temp = 0
        if temp >= 5:
            roman_output += RomanNumerals.value_to_symbol[50]
            temp -= 5
        if temp == 4:
            roman_output += RomanNumerals.value_to_symbol[10]
            roman_output += RomanNumerals.value_to_symbol[50]
            temp -= 4
        if temp in range(1, 4):
            for i in range(temp):
                roman_output += RomanNumerals.value_to_symbol[10]

        # Process ones place.
        ones_digit = int(val_string[-1])
        temp = ones_digit
        if temp == 9:
            roman_output += RomanNumerals.value_to_symbol[1]
            roman_output += RomanNumerals.value_to_symbol[10]
            temp = 0
        if temp >= 5:
            roman_output += RomanNumerals.value_to_symbol[5]
            temp -= 5
        if temp == 4:
            roman_output += RomanNumerals.value_to_symbol[4]
            temp -= 4
        if temp in range(1, 4):
            for i in range(temp):
                roman_output += RomanNumerals.value_to_symbol[1]





        return roman_output 

    def from_roman(roman_num):
        return 0
