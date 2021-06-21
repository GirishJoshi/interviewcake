"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our 
Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our 
lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))

"""


def merge_lists(firstlist, secondlist):

    merged_list = []
    first_index, second_index = 0, 0

    # this loop will run until we exhaust one of the list
    while first_index < len(firstlist) and second_index < len(secondlist):

        if firstlist[first_index] < secondlist[second_index]:
            merged_list.append(firstlist[first_index])
            first_index += 1
        else:
            merged_list.append(secondlist[second_index])
            second_index += 1

    # add the rest of the elements to our merged list
    if first_index < len(firstlist):
        merged_list = merged_list + firstlist[first_index:]
    else:
        merged_list = merged_list + secondlist[second_index:]

    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 3, 6, 12, 14, 19]

print(merge_lists(my_list, alices_list))
