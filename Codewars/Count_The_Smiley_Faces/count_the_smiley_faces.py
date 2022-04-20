# File: count_the_smiley_faces.py
'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example:
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note:
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.
'''
def count_smileys(arr):
    smiley_count = 0
    valid_eyes = [':', ';']
    valid_noses = ['-', '~']
    valid_mouths = [')', 'D']
    smiley_list = list(arr)
    for s in smiley_list:
        if len(s) == 2:
            if s[0] in valid_eyes and s[1] in valid_mouths:
                smiley_count += 1
        elif len(s) == 3:
            if s[0] in valid_eyes and\
                    s[1] in valid_noses and\
                    s[2] in valid_mouths:
                smiley_count += 1
        else:
            pass

    return smiley_count
