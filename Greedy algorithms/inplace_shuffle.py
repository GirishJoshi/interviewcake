import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def inplace_shuffle(the_list):

    last_index = len(the_list) - 1

    for current_index in range(len(the_list) - 1):

        random_index = get_random(current_index, last_index)

        if current_index != random_index:
            the_list[current_index], the_list[random_index] = (
                the_list[random_index],
                the_list[current_index],
            )

    return the_list


the_list = [1, 2, 3, 4, 5]
print(inplace_shuffle(the_list))
