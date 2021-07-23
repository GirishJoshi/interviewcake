list_of_ints = [5, 3, 4, -9, 7, 3, 1]


def highest_prod_2(list_of_ints):

    max_prod_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    highest_prod_2 = list_of_ints[0] * list_of_ints[1]
    lowest_prod_2 = list_of_ints[0] * list_of_ints[1]

    high = max(list_of_ints[0], list_of_ints[1])
    low = min(list_of_ints[0], list_of_ints[1])

    for num in list_of_ints[1:]:

        max_prod_3 = max(max_prod_3, highest_prod_2 * num, lowest_prod_2 * num)

        highest_prod_2 = max(highest_prod_2, num * high, num * low)
        lowest_prod_2 = min(lowest_prod_2, num * high, num * low)

        high = max(high, low, num)
        low = min(high, low, num)

    return max_prod_3


print(highest_prod_2(list_of_ints))
