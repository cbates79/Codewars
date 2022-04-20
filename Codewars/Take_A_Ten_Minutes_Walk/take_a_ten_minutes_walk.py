# File: take_a_ten_minutes_walk.py
'''
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take 
the opportunity to go for a short walk. The city provides its citizens with a 
Walk Generating App on their phones -- everytime you press the button it 
sends you an array of one-letter strings representing directions to 
walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for 
each letter (direction) and you know it takes you one minute to traverse 
one city block, so create a function that will return true if the walk the 
app gives you will take you exactly ten minutes (you don't want to be 
early or late!) and will, of course, return you to your starting point. 
Return false otherwise.

Note: you will always receive a valid array (string in COBOL) containing a 
random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's 
standing still!).
'''
def is_valid_walk(walk):
    valid_walk_time = 10
    walk_list = list(walk)
    walk_time = len(walk_list)
    n_count = walk_list.count('n')
    s_count = walk_list.count('s')
    e_count = walk_list.count('e')
    w_count = walk_list.count('w')
    is_time_valid = bool(walk_time == valid_walk_time)
    is_ns_equal = bool(n_count == s_count)
    is_ew_equal = bool(e_count == w_count)
    return is_time_valid and is_ns_equal and is_ew_equal
