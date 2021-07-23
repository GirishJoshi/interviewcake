"""
You have a list of integers, and for each index you want to find the product of 
every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of 
integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
"""

int_list = [1, 7, 3, 4]


def get_products_of_all_ints_except_at_index(int_list):

    if len(int_list) < 2:
        raise IndexError(
            "Getting the product of numbers at other "
            "indices requires at least 2 numbers"
        )

    product_of_all_ints_except_at_index = [None] * len(int_list)

    product_so_far = 1
    for i in range(len(int_list)):
        product_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        product_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return product_of_all_ints_except_at_index


print(get_products_of_all_ints_except_at_index(int_list))
