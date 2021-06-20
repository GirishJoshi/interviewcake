"""
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break 
into a major European National Cake Vault. The message has been mostly deciphered, 
but all the words are backward! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and reverses 
the order of the words in place.

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. 
Since we're modifying the message, we need a mutable ↴ type like a list, 
instead of Python 2.7's immutable strings.

For example:

  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print ''.join(message)

When writing your function, assume the message contains only letters and spaces, 
and all words are separated by one space.
"""


def reverse_words(message):

    # reverse all characters in the entire message
    reverse_characters(message, 0, len(message) - 1)

    # we'll hold the index of *start* of current word
    # as we look for the index of *end* of current word
    current_start = 0

    for i in range(len(message) + 1):

        # !Found end of the current word
        if (i == len(message)) or (message[i] == " "):
            reverse_characters(message, current_start, i - 1)
            current_start = i + 1


def reverse_characters(message, start, end):

    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1


message = [
    "c",
    "a",
    "k",
    "e",
    " ",
    "p",
    "o",
    "u",
    "n",
    "d",
    " ",
    "s",
    "t",
    "e",
    "a",
    "l",
]

reverse_words(message)

# laets dnuop ekac

# Prints: 'steal pound cake'
print("".join(message))
