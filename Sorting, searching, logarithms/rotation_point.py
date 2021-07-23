"""
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, 
looking for words I didn't know. I put each word I didn't know at increasing indices in 
a huge list I created in memory. When I reached the end of the dictionary, 
I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere 
in the middle of the alphabet, reach the end, and then start from the beginning of 
the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." 

For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I 
started working from the beginning of the dictionary. This list is huge 
(there are lots of words I don't know) so we want to be efficient here.
"""


words = [
    "ptolemaic",
    "retrograde",
    "supplant",
    "undulate",
    "xenoepist",
    "asymptote",  # <-- rotates here!
    "babka",
    "banoffee",
    "engender",
    "karpatka",
    "othellolagkage",
]

# words = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]


def rotation_point(words):

    floor_index = -1
    ceiling_index = len(words) - 1

    while floor_index + 1 < ceiling_index:

        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        top = words[guess_index - 1]
        center = words[guess_index]
        bottom = words[guess_index + 1]

        print(center)

        if center < top and center < bottom:
            return guess_index

        if center > top and center < bottom:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index

    return False


print(rotation_point(words))
