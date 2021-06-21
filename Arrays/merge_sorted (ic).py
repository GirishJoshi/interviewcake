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

# Note: the if condition is really awesome, it's based on DRY principle.


def merge_sorted(firstlist, secondlist):
    # Set up merged list
    merged_list_size = len(firstlist) + len(secondlist)
    merged_list = [None] * merged_list_size

    first_index, second_index, merged_index = 0, 0, 0

    while merged_index < merged_list_size:
        is_firstlist_exhausted = first_index >= len(firstlist)
        is_secondlist_exhausted = second_index >= len(secondlist)

        if (not is_firstlist_exhausted) and (
            is_secondlist_exhausted or firstlist[first_index] < secondlist[second_index]
        ):
            # Case: next comes from first list
            # first list must not be exhausted, and EITHER:
            # 1) second list IS exhausted, or
            # 2) the current element in first list is less than the current element in second list
            merged_list[merged_index] = firstlist[first_index]
            first_index += 1
        else:
            # Case: next comes from second list
            merged_list[merged_index] = secondlist[second_index]
            second_index += 1

        merged_index += 1

    return merged_list


my_list = [3, 4, 6, 10, 11, 26]
alices_list = [1, 5, 8, 12, 14, 19, 20, 21, 22]

print(merge_sorted(my_list, alices_list))
