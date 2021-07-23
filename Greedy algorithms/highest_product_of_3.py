"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""
list_of_ints = [5, 3, 4, -9, -7, 1]
# list_of_ints = [5, 3]


def highest_product_of_3_with_sorted(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError("Require at least three integers in the list")

    prod_of_3 = sorted(list_of_ints[:3])

    for num in list_of_ints[3:]:

        if num > prod_of_3[0]:
            prod_of_3[0] = num
            prod_of_3 = sorted(prod_of_3)

    return prod_of_3


def highest_product_of_3(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError("Require at least three integers in the list")

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    max_prod_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for current_num in list_of_ints[2:]:

        max_prod_3 = max(
            max_prod_3,
            highest_product_of_2 * current_num,
            lowest_product_of_2 * current_num,
        )

        highest_product_of_2 = max(
            highest_product_of_2, current_num * highest, current_num * lowest
        )

        lowest_product_of_2 = min(
            lowest_product_of_2, current_num * highest, current_num * lowest
        )

        highest = max(highest, current_num)
        lowest = min(lowest, current_num)

    return max_prod_3


def highest_product_of_4(list_of_ints):

    if len(list_of_ints) < 4:
        raise ValueError("Need atleast 4 values.")

    max_prod_4 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2] * list_of_ints[3]
    high_prod_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    low_prod_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    high_prod_2 = list_of_ints[0] * list_of_ints[1]
    low_prod_2 = list_of_ints[0] * list_of_ints[1]

    high = max(list_of_ints[0], list_of_ints[1])
    low = min(list_of_ints[0], list_of_ints[1])

    for num in list_of_ints[2:]:

        max_prod_4 = max(max_prod_4, high_prod_3 * num, low_prod_3 * num)

        high_prod_3 = max(high_prod_3, high_prod_2 * num, low_prod_2 * num)
        low_prod_3 = min(low_prod_3, high_prod_2 * num, low_prod_2 * num)

        high_prod_2 = max(high_prod_2, high * num, low * num)
        low_prod_2 = min(low_prod_2, high * num, low * num)

        high = max(high, num)
        low = min(low, num)

    return max_prod_4


def multipy_first_k(list_of_ints, k):

    prod_of_k = 1
    for i in range(k):
        prod_of_k = prod_of_k * list_of_ints[i]

    return prod_of_k


def highest_product_of_k(list_of_ints, k):

    if len(list_of_ints) < k:
        raise ValueError(f"Need atleast {k} integers")

    max_prod_k = multipy_first_k(list_of_ints, k)
    # print(max_prod_k)
    high_prods = []
    low_prods = []

    for index in reversed(range(2, k)):
        # print(index)
        prod = multipy_first_k(list_of_ints, index)
        high_prods.append(prod)
        low_prods.append(prod)

    high_prods.append(max(list_of_ints[0], list_of_ints[1]))
    low_prods.append(min(list_of_ints[0], list_of_ints[1]))

    print(high_prods)
    print(low_prods)

    for i in range(k - 2, len(list_of_ints)):

        num = list_of_ints[i]

        print(f">{num}")
        max_prod_k = max(max_prod_k, high_prods[0] * num, low_prods[0] * num)
        print(max_prod_k, high_prods[0] * num, low_prods[0] * num)

        for i in range(k - 2):
            print(f">>{i}")
            high_prods[i] = max(
                high_prods[i], high_prods[i + 1] * num, low_prods[i + 1] * num
            )
            low_prods[i] = min(
                low_prods[i], high_prods[i + 1] * num, low_prods[i + 1] * num
            )

        high_prods[-1] = max(high_prods[-1], num)
        low_prods[-1] = min(low_prods[-1], num)

    return max_prod_k


print(highest_product_of_k(list_of_ints, 5))
