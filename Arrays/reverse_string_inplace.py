"""
Write a function that takes a list of characters and reverses the letters in place.
"""

# no_strings_attached is a list of characters
def reverse_string_inplace(no_strings_attached):

    start = 0
    end = len(no_strings_attached) - 1

    while start < end:

        no_strings_attached[start], no_strings_attached[end] = (
            no_strings_attached[end],
            no_strings_attached[start],
        )

        start += 1
        end -= 1

    return no_strings_attached


print(reverse_string_inplace(["n", "o", "s", "t", "r", "i", "n", "g", "a"]))
