"""
Write an efficient function that checks whether any permutation of an input string is a palindrome.

A palindrome is a string that's the same when read forward and backward.

Examples:

civic
mom
anna
kayak
racecar

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"But 'ivicc' isn't a palindrome!"

If you had this thought, read the question again carefully. 
We're asking if any permutation of the string is a palindrome. 
Spend some extra time ensuring you fully understand the question before starting. 
Jumping in with a flawed understanding of the problem doesn't look good in an interview.
"""


def has_palindrome_permutation(word):

    w_dict = {}.fromkeys(list(word), 0)

    for w in word:
        w_dict[w] = w_dict[w] + 1

    print(w_dict)

    if len(word) % 2 != 0:
        for key in w_dict:
            if w_dict[key] % 2 != 0:
                w_dict[key] = w_dict[key] - 1
                break

    print(w_dict)
    for key in w_dict:
        if w_dict[key] % 2 != 0:
            return False
    return True


print(has_palindrome_permutation("livci"))
