# File: nesting_structure_comparison.py
'''
Complete the function/method (depending on the language) to return true/True 
when its argument is an array that has the same nesting structures and same 
corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''
def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    elif type(original) == list and type(other) == list:

        


    else:
        print("Error. Fell through")
















'''
    try:
        original_list = list(original)
    except TypeError:
        original_list = list()
        original_list.append(original)
    try:
        other_list = list(other)
    except TypeError:
        other_list = list()
        other_list.append(other)
'''
'''
    same_structure = True

    # For testing:
    print(f"len(original_list) == {len(original_list)}")
    print(f"len(other_list) == {len(other_list)}")
    if len(original) != len(other):
        same_structure = False
        return same_structure
    elif len(original_list) == len(other_list) and len(other_list) == 1:
        same_structure = True
        return same_structure
    elif len(original_list) == len(other_list) and len(other_list) > 1:
        counter = len(original_list)
        for i in range(counter):
    else:
        print("Error. Fell Through.")
'''


'''    elif len(original_list) == 0 and len(original_list) == len(other_list): 
        return same_structure
    elif len(original_list) > 0 and len(original_list) == len(other_list): 
        length = len(original_list)
        for i in range(length):
            if not same_structure_as(original_list[i], other_list[i]):
                same_structure = False 
                return same_structure
        else:
            return same_structure
    else:
        print('Error. Fell through without returning a boolean.')
'''
