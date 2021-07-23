"""
Find a duplicate, Space Edition™.

We have a list of integers, where:

The integers are in the range 1..n
The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. 
But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. 
(If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. 
Thing is, the damn thing came with the RAM soldered right to the motherboard, 
so we can't upgrade our RAM. So we need to optimize for space!
"""

the_list = [5, 6, 2, 1, 7, 2, 10, 11, 2]


def find_duplicate_space(the_list):

    the_list = sorted(the_list)

    floor_index = 0
    ceiling_index = len(the_list) - 1

    while floor_index + 1 < ceiling_index:

        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

    print(the_list)


print(find_duplicate_space(the_list))
